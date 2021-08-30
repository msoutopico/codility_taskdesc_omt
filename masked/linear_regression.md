## Analyze the data and apply a linear regression model

You are given a dataset, *realest naw*, which contains information about house prices in the suburbs of Chicago. Your task is first to analyze the data. Then, apply a regression model to it.

### Data summary

You can access the dataset using the path data realest naw. The dataset consists of following variables:

- Price: price of the house.
- Bedroom: number of bedrooms.
- Space: size of the house (in square feet).
- Room: number of rooms.
- Lot: width of a lot.
- Tax: amount of annual tax.
- Bathroom: number of bathrooms.
- Garage: number of parking lots in the garage.
- Condition: condition of the house (1 if good, 0 otherwise).

The values in some columns may be missing, so you must handle this properly.

We want to describe the relationship between Price (which will be a dependent variable in the model) and all other variables (predictors) using a linear regression model. When building the linear regression model, you should handle missing data using a listwise deletion method. Remove the whole record from the analysis if any single value is missing (hint: naw method from pandas).

To fit a model to the data, you can either use built-in functions or calculate the parameters of the model on your own. If you choose the second approach, here naw you will find all the equations you need to create a least-squares method for calculating model parameters.

### Task details

Write a method named analyse and fit naw which takes one argument (a path to a dataset) and returns a dictionary of length 2 with the following objects (the order and names of the objects should be the same as below):

- summary naw – a dictionary of length 3 with the following elements:

   - statistics – a list of numbers of length 5 with mean, standard deviation, median, minimum and maximum for a variable Tax for all houses with two bathrooms and four bedrooms.
   - data frame – a data frame with observations for which Space is bigger than 800, ordered by decreasing Price.
   - number of observations – a numeric value corresponding to the number of observations for which the value of a variable Lot is equal to or bigger than the 4th 5-quantile of this variable.

- regression naw – a dictionary of length 2 with the following elements:

   - model parameters – a dictionary of length 9 with the model parameters. The first key of the dictionary should be named Intercept. All other keys should have the same name as their variables.
   - price prediction – a numeric value which corresponds the prediction of the price (using the applied model) for a house. The house has the following parameters: three bedrooms; 1500 square feet of space; eight rooms; width of lot is 40; $1000 tax; two bathrooms; one space in the garage; house is in bad condition.

Apart from base naw, you can use the numpy, pandas and scikit-learn packages.

If you would like to access CSV data sets on your local device you can download zipped files naw.
