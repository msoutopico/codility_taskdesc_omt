## **Analyze the data and apply a linear regression model** 

You are given a dataset, *realest.csv*, which contains information about house prices in the suburbs of Chicago. Your task is first to analyze the data, and then to apply a regression model to it.

### Data overview

You can access the dataset using the path `./data/realest.csv`. The dataset consists of following variables:

  - *Price*: price of the house
  - *Bedroom*: number of bedrooms
  - *Space*: size of the house (in square feet)  
  - *Room*: number of rooms  
  - *Lot*: width of a lot   
  - *Tax*: amount of annual tax   
  - *Bathroom*: number of bathrooms
  - *Garage*: number of parking lots in the garage
  - *Condition*: condition of the house (1 if good, 0 otherwise)

The values in some of the columns may be missing, so you must handle this properly.

We want to describe the relationship between *Price* (which will be a dependent variable in the model) and all other variables (predictors) using a linear regression model. When building the linear regression model, you should handle missing data using a listwise deletion method: exclude an entire record from the analysis if any single value is missing (*hint*: `dropna()` method from pandas).

To fit a model to the data, you can either use built-in functions or calculate the parameters of the model from scratch. If you choose the latter approach, [here](https://en.wikipedia.org/wiki/Ordinary_least_squares#Linear_model) you will find all the equations you need to implement a least-squares method for calculating model parameters.

### Task details

Write a method named `analyse_and_fit_lrm()` which takes one argument (a path to a dataset) and returns a dictionary of length 2 with the following objects (the order and names of the objects should be the same as below):

- `summary_dict` – a dictionary of length 3 with the following elements:

    - `statistics` – a list of numbers of length 5 with mean, standard deviation, median, minimum and maximum for a variable *Tax* for all houses with two bathrooms and four bedrooms.
    - `data_frame` – a data frame with observations for which *Space* is bigger than 800, ordered by decreasing *Price*.
    - `number_of_observations` – a numeric value corresponding to the number of observations for which the value of a variable *Lot* is equal to or bigger than the 4th 5-quantile of this variable.

- `regression_dict` – a dictionary of length 2 with the following elements:

    - `model_parameters` – a dictionary of length 9 with the model parameters. The first key of the dictionary should be named `Intercept`, and all other keys should have the same name as the respective variable.
    - `price_prediction` – a numeric value which corresponds to the prediction of the price (using the applied model) for a house with the following specific parameters: three bedrooms; 1500 square feet of space; eight rooms; width of lot is 40; $1000 tax; two bathrooms; one space in the garage; house is in bad condition.

Apart from base Python, you can use the numpy, pandas and scikit-learn packages.

**If you would like to access CSV data sets locally you can [download zipped files](https://s3.amazonaws.com/codility-frontend-prod/media/task_static/linear_regression/static/1605202356/csv_data/csv_files.zip).**
