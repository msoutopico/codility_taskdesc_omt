Create a function `get_recommendations` which will take as arguments three dataframes, a name for the user, the year of interest and the recommendation method, and will return the title of the most highly recommended movie for the given user.

The function `get_recommendations` takes as arguments three dataframes: `users`, `movies` and `ratings`, with the following structure:.

- `users` – information about users with the columns: `user id`, `full name`, `age`, `gender` and `zip code`;
- `ratings` – information about movie ratings by users (only one movie's evaluation per user) with the columns: `user id`, `item id`, `rating` and `timestamp`;
- `movies` – information about movies with the columns: `movie id` (should match `item_id` from `ratings`), `movie title` and `release year`.

The next three arguments are: `full name`, `year` and `method`.
`Full name` is the full name of the user for whom we want to return one recommended movie whose release year is equal to `year` using one of the three implemented `method`s:
- By `method=by_popularity` return the movie title with the most ratings.
- By `method=by_rating` return the movie title with the highest average rating.
- By `method=by_similar_users` return the movie title with the latest rating (timestamp) among a group of similar users to a given user. A group of similar users are users who have seen at least one movie that the given user has seen, and for which the maximum difference between their rating and the given user's rating of the same movie is 1 (for every movie they have both seen). You can use function `check_similar_users` or create own implementation.
The `check_similar_users` function returns True if users with ids: `users_id_x`, `user_id_y` are similar based on ratings dataframe and False otherwise.

All methods should return a movie title that has not been rated by the given user.

If there is more than one movie that meets the condition (e.g. more than one movie with the same highest average rating in `method=by_rating`), the function should return the first movie in alphabetical order.

For the cases listed below the function should return an empty string:
- given `full name` or a `year` does not exist in the given data
- inappropriate `method` argument
- after applying year filtering all movies are already rated by the user
- there doesn't exist any user similar to the user

### Packages versions
Additionally, to Python 3.8 standard library you can use following packages:
- pandas 0.25.3


### Examples

For the example dataframes displayed below:

```
|user id |full name      |age |gender |zip code |
|--------|---------------|----|-------|---------|
|1       |Ryan James     |24  |M      |85711    |
|2       |Alice Graves   |53  |F      |94043    |
|3       |Ambrose Smith  |23  |M      |32067    |
|4       |Bobby Alvarez  |24  |M      |90412    |
|5       |Latosha Jiles  |53  |F      |15343    |
|6       |Louis Mcmillen |23  |M      |74920    |
```

```
|user id |item id |rating |timestamp |
|--------|--------|-------|----------|
|2       |1       |1      |881250949 |
|3       |1       |2      |891717742 |
|4       |1       |2      |878887116 |
|5       |1       |3      |894528467 |
|3       |2       |5      |886397596 |
|4       |2       |4      |884182806 |
|1       |3       |2      |881171488 |
|2       |3       |2      |891628467 |
|1       |4       |5      |886324817 |
|2       |4       |3      |883603013 |
|1       |5       |5      |879372434 |
|3       |5       |5      |879781125 |
|3       |4       |4      |876042340 |
|4       |4       |5      |891035994 |
|4       |5       |5      |898603000 |
|2       |5       |5      |904528467 |
|4       |6       |4      |894528467 |
```

```
|movie id |movie title             |release year |
|---------|------------------------|-------------|
|1        |Toy Story (1995)        |1995         |
|2        |GoldenEye (1995)        |1995         |
|3        |Four Rooms (1995)       |1995         |
|4        |Get Shorty (1995)       |1995         |
|5        |Dead Man Walking (1995) |1995         |
|6        |Postino, Il (1994)      |1995         |
```

- The output for `get_recommendations(users, movies, ratings, full_name='Ryan James',method='by_popularity', year=1995)` would be _'Toy Story (1995)'_.
- The output for `get_recommendations(users, movies, ratings, full_name='Ryan James',method='by_rating', year=1995)` would be _'GoldenEye (1995)'_.
- The output for `get_recommendations(users, movies, ratings, full_name='Ryan James',method='by_similar_users', year=1995)` would be _'Postino, Il (1994)'_.

**If you would like to access CSV data sets locally you can [download zipped files](https://s3.amazonaws.com/codility-frontend-prod/media/task_static/recommendation_system/static/1615289452/csv_data/csv_files.zip).**
