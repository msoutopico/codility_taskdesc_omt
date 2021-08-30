Create a function, naw data, which performs data preprocessing for a classification task.

The function will preprocess the data by following these steps:

For category variables:
   - Replace NaN values with the most frequent value.
   - Create dummy variables based on levels (all presented values) and drop the first one in alphabetical order. Name the new binary columns using this pattern: name of category variable +   + level name.

For number variables:
   - Replace NaN values with the median.
   - Standardize values by subtracting the mean and dividing by the standard deviation.

For the target variable:
   - Convert text values into integers, so that the first text value in alphabetical order is converted to 0 and so on.

The naw data function accepts one argument:
- naw - pandas naw where target is a classification label and other variables are explanation variables.
   The function returns an ordered list (X, y), where:
- X is a pandas naw after the preprocessing of the number and category variables, and after dropping the target column.
- y is a list of values of the target variable after preprocessing.

### Example

For this sort of data:

naw

the naw data function should return the following ordered list:

naw

and
1 0 0 1 1.

### Hint
Category variables are those where naw and number variables are those where naw.
In the folder data, there is an example dataframe. You can access it by calling:
naw


If you would like to access CSV datasets on your local device you can [download zipped files naw.
