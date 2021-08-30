Write three Python functions, register them as PySpark UDF functions and use them to produce an output dataframe.

* **NOTE: This task runs against Spark version 2.4.5.**

The input file `birds.csv` contains data from the UK Department for Environment, Food and Rural Affairs and shows
the annual change in the number of birds of each species living in the United Kingdom.

Here are five rows picked at random from this file:
```
+----------------------------------------------+-----------------------+-----------+------------------------+
|Species                                       |Category               |Period     |Annual percentage change|
+----------------------------------------------+-----------------------+-----------+------------------------+
|Greenfinch (Chloris chloris)                  |Farmland birds         |(1970-2014)|-1.13                   |
|Siskin (Carduelis spinus)                     |Woodland birds         |(1995-2014)|2.26                    |
|European shag (Phalacrocorax artistotelis)    |Seabirds               |(1986-2014)|-2.31                   |
|Mute Swan (Cygnus olor)                       |Water and wetland birds|(1975-2014)|1.65                    |
|Collared Dove (Streptopelia decaocto)         |Other                  |(1970-2014)|5.2                     |
+----------------------------------------------+-----------------------+-----------+------------------------+
```

The `Species` column contains both English and Latin names as raw data using this format: `English Name (Latin Name)`.

The `Period` column contains a date range in years as raw data using this format: `(start_year-end_year)`.

#### Requirements

Please create the following three functions in the `udfs.py` file:

`get_english_name` – this function should get the `Species` column value and return the English name.

`get_start_year` – this function should get the `Period` column value and return the year (an integer) when data collection began.

`get_trend` – this function should should get the `Annual percentage change` column value and return the change trend category based on the following rules:

- Annual percentage change less than -3.00 – return 'strong decline';
- Annual percentage change between -3.00 and -0.50 (inclusive) – return 'weak decline';
- Annual percentage change between -0.50 and 0.50 (exclusive) – return 'no change';
- Annual percentage change between 0.50 and 3.00 (inclusive) – return 'weak increase';
- Annual percentage change more than 3.00 – return 'strong increase'.

Then, in the same file `udfs.py`, please register these functions as PySpark UDF functions (under the same names as Python functions) so they can be used in PySpark.

After doing that, please update `transform` method inside `job.py`. This method accepts a raw dataframe as an input and should use the functions created above to transform the data to the following format:
```
+------------+-----------------------+-------------------+------------------------+-------------+
|species     |category               |collected_from_year|annual_percentage_change|trend        |
+------------+-----------------------+-------------------+------------------------+-------------+
|Reed Warbler|Water and wetland birds|1981               |1.72                    |weak increase|
+------------+-----------------------+-------------------+------------------------+-------------+
```

The `species` column should use the `get_english_name` function and the `Species` column as input.

The `collected_from_year` column should use the `get_start_year` function and the `Period` column as input.

The `trend` column should use the `get_trend` function and the `Annual percentage change` column as input.

Here are the names of the columns that should be included in the dataframe returned by the `transform` method:

```
species, category, collected_from_year, annual_percentage_change, trend
```

Please make sure that the columns are named correctly.

#### Hint

If you would like to use lambda expression when registering the functions as UDFs, please remember that the function passed as an argument needs to have a different name. In this case you can modify the initial function name (e.g. change `get_trend` to `get_trend_unregistered`), just make sure that in the end, the function registered as UDF is named properly (in this case: `get_trend`).

**If you would like to access CSV data sets locally you can [download zipped files](https://s3.amazonaws.com/codility-frontend-prod/media/task_static/pyspark_udf_birds/static/1596810710/csv_data/csv_files.zip).**
