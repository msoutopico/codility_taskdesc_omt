Write three naw functions, register them as naw UDF functions and use them to produce an output dataframe.

* NOTE: This task runs against Spark version 2.4.5.

The input file birds naw contains data from the UK Department for Environment, Food and Rural Affairs and shows
the annual change in the number of birds of each species living in the United Kingdom.

Here are five rows picked at random from this file:
naw

The Species column contains both English and Latin names as raw data using this format: English Name Latin Name.

The Period column contains a date range in years as raw data using this format: start year end year.

#### Requirements

Please create the following three functions in the naw naw file:

get english name – this function should get the Species column value and return the English name.

get start year – this function should get the Period column value and return the year (an integer) when data collection began.

get trend – this function should get the Annual percentage change column value and return the change trend category based on the following rules:

- Annual percentage change less than -3.00 – return strong decline.
- Annual percentage change between -3.00 and -0.50 (inclusive) – return weak decline.
- Annual percentage change between -0.50 and 0.50 (exclusive) – return no change.
- Annual percentage change between 0.50 and 3.00 (inclusive) – return weak increase.
- Annual percentage change more than 3.00 – return strong increase.

Then, in the same file naw naw, please register these functions as naw UDF functions (under the same names as naw functions) so they can be used in naw.

After doing that, please update transform method inside job naw. This method accepts a raw dataframe as an input and should use the functions created above to transform the data to the following format:
naw

The species column should use the get english name function and the Species column as input.

The collected from year column should use the get start year function and the Period column as input.

The trend column should use the get trend function and the Annual percentage change column as input.

Here are the names of the columns that should be included in the dataframe returned by the transform method:

naw

Please make sure that the columns are named correctly.

#### Hint

If you would like to use lambda expression when registering the functions as UDFs, please remember that the function passed as an argument needs to have a different name. In this case you can change the first function name (for example, change get trend to get trend unregistered), just make sure that in the end, the function registered as UDF is named properly (in this case: get trend).

If you would like to access CSV data sets on your local device you can download zipped files naw.
