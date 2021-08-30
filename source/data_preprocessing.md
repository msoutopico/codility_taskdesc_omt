Create a function, `preprocess_data`, which performs data preprocessing for a classification task.

The function will preprocess the data by performing the following steps:

1. For categorical variables:
    - replace NaN values with the most frequent value;
    - create dummy variables based on levels (all presented values) and drop the first one in alphabetical order. Name the new binary columns using this schema: name of categorical variable + _ + level name.

2. For numerical variables:
    - replace NaN values with the median;
    - standardize values by subtracting the mean and dividing by the standard deviation.

3. For the `target` variable:
    - convert text values into integers, so that the first text value alphabetically is converted to 0 and so on.

The `preprocess_data` function accepts one argument:
- `dataframe` - pandas DataFrame where `target` is a classification label and other variables are explanatory variables.
The function returns a tuple (X, y), where:
- X is a pandas DataFrame obtained after performing the preprocessing of numerical and categorical variables and after dropping the target column;
- y is a list of values of the target variable after preprocessing.

### Example

For this sort of data:

```
|target  |married |degree |salary |occupation|
|--------|--------|-------|-------|----------|
|male    |0       |1      |1.5    |nurse     |
|female  |1       |2      |NaN    |nurse     |
|female  |1       |3      |2.3    |policeman |
|male    |1       |2      |2.0    |fireman   |
|male    |0       |3      |1.5    |NaN       |
```

the `preprocess_data` function should return the following tuple:

```
|married_1 |degree_2 |degree_3 |occupation_nurse |occupation_policeman |salary  |
|----------|---------|---------|-----------------|---------------------|--------|
|0         |0        |0        |1                |0                    |-1.00896|
|1         |1        |0        |1                |0                    |-0.19528|
|1         |0        |1        |0                |1                    |1.59481 |
|1         |1        |0        |0                |0                    |0.61840 |
|0         |0        |0        |1                |0                    |-1.00896|
```

and
`[1, 0, 0, 1, 1]`.

### Hint
Treat variables as categorical when `dtype = 'category'` and as numerical when `dtype = 'float64'`.
In the folder data, there is an exemplary dataframe. You can access it by calling:
```
pd.read_csv(
    "data/example_data.csv",
    dtype={
        "target": object,
        "checking_account_status": "category",
        "duration": np.float64,
        "credit_history": "category",
        "credit_amount": np.float64,
        "other_installment_plans": "category",
        "job": "category",
        "foreign_worker": "category",
        "interest_rate": np.float64,
        "city": "category",
    },
)
```


**If you would like to access CSV data sets locally you can [download zipped files](https://s3.amazonaws.com/codility-frontend-prod/media/task_static/data_preprocessing/static/1615210571/csv_data/csv_files.zip).**
