For this task, you will deal with ratings given by users to movies (films) that they have seen. A rating is a vote from 1 to 5 based on how much the user liked the movie and recommends it to other users. Create a function get recommendations which will take as arguments three dataframes: a name for the user, the release year, and the recommendation method. The function returns the title of the most highly recommended movie for the given user.

The function get recommendations takes as arguments three dataframes: users, movies and ratings, with the following structure:

- users â€“ information about users with the columns: user id, full name, age, gender and zip code.
- ratings â€“ information about movie ratings by users (only one movie’s rating per user) with the columns: user id, item id, rating and timestamp.
- movies â€“ information about movies with the columns: movie id (should match item id from ratings), movie title and release year.

The next three arguments are: full name, year and method.
Full name is the full name of the user for whom we want to return one recommended movie whose release year is equal to year using one of the three methods:
- By method by popularity return the movie title with the most ratings.
- By method by rating return the movie title with the highest average rating.
- By method by similar users return the movie title with the latest rating (timestamp) among a group of similar users to a given user. A group of similar users are users who have seen at least one movie that the given user has seen. Also, the maximum difference between their rating and the given user’s rating of the same movie is 1 (for every movie they have both seen). You can use function check similar users or create your own.
   The check similar users function returns True if users with ids: users id naw, user id y are similar based on ratings dataframe and False otherwise.

All methods should return a movie title that has not been rated by the given user.

It can happen that more than one movie meets the condition. For example, several movies have the same highest average rating in method by rating). In such a case, the function should return the first movie in alphabetical order.

For the cases listed below the function should return an empty string:
- given full name or a year does not exist in the given data.
- incorrect method argument.
- after applying year filtering all movies are already rated by the user.
- there doesn’t exist any user similar to the user.

### Packages versions
You can use the following package besides the naw 3.8 standard library:
- pandas 0.25.3


### Examples

For the example dataframes displayed below:

naw

naw

naw

- The output for get recommendations users movies ratings full name James method popularity year 1995 would be  Toy Story (1995) .
- The output for get recommendations users movies ratings full name James method rating year 1995 would be  naw (1995) .
- The output for get recommendations users movies ratings full name James method similar users year 1995 would be  Postino, Il (1994) .

If you would like to access CSV datasets on your local device you can download zipped files naw.
