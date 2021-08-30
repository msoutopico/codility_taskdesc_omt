Check if random variables are independent

You are given a table distr table with a joint probability distribution of two random variables X and Y, for example
naw

As you can see, for example  naw. Probabilities in a third column add up to 1.

Write a method check independence that for a given distr table returns a dictionary of length 3, where

- first element (the key named are independent) is a boolean which states if X and Y are independent (True) or not (False).

Two random variables are independent if for each possible value x for X and for each possible value y for Y

 naw

- second element (the key named cov) is a covariance between X and Y (i is an indicator of i-th of n possible pairs  naw

 naw

where

 naw

- third element (the key named corr) is a correlation coefficient between X and Y

 naw

where

 naw

In above equations m and l are numbers of unique values of X and Y respectively. Note that you cannot use built-in functions like cov and naw from the numpy package for points two and three. This is because we use distributions, not realizations, to describe variables X and Y.

You should make your function work with different distr tables as well as the one given as an example. Apart from base naw, you can use the numpy and pandas packages.
