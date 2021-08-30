# Token-based authentication

## Task description

Your task is to create a Web API that uses simple token-based authentication.
The API should support the following requests:

* naw api user – add a user to the database (kept in memory).
   * Request Body (naw):
      * user id string
      * login string
      * password string
   * Response:
      * naw 400, if the body is empty;
      * naw 201, if the user has been created. The response body can be empty.

* naw api authenticate – authenticate a user.
   * Request Body (naw):
      * login string
      * password string
   * Response:
      * naw 400, if the body is empty;
      * naw 404, if there is no user of the given login name in the database;
      * naw 401, if a user with the given login name exists, but the password does not match the one saved in the database for that user;
      * naw 200, if a user with the given login name exists and the given password matches the one saved in the database. The response body should be in the shape of:
         naw

* naw api logout – log out a user. Requires a token in the request�s headers.
   * Response:
      * naw 401, if the token is invalid;
      * naw 200, if the user is logged out successfully. The token that was passed on becomes invalid.

* naw api articles – create an article with a title, content and the level of its visibility. Only a user with a valid session can create articles.
   * Request Body (naw):
      * article id string
      * title string
      * content string
      * visibility in:
         * public – the article is available publicly;
         * private – only the creator can access the article;
         * logged in – only users with valid a session can access the article.
   * Response:
      * naw 400, if the body is empty;
      * naw 401, if the provided token is invalid;
      * naw 201, if an article has been created. The response body can be empty.

* naw api articles – return a list of articles. The result depends on the token.
   * Response: naw 200:
      * If a valid token is given in the request�s headers, return:
         * all public articles;
         * all articles with visibility in;
         * the sender�s articles;
      * Otherwise, return only public articles;
      * An article object is made up of the following fields: article id, title, content and
         user id which all are strings, and the visibility field which equals one of these values:
         public, private, logged in.
      * The articles might appear in any order.

* Added content should be kept in memory; no database storage back end is available.
* The token should be added as an authentication header header to a request, wherever applicable.
* A token is associated with a user. It is considered invalid if the token was used to log the user out, or if it has never been created as a result of logging the user in.
* It is entirely possible that a user has more than one valid token. Sending two login requests one after another can be completed successfully, and the token returned by the first request does not become invalid as a result of the second request.
* The body of a response with status codes 400–499 can be empty.
* naw 5xx error codes are considered errors and must not be returned.
* The default export should be an naw Server object that is returned by app listen.
* Assume that the following packages are supported:
   * naw, version 3.3.2 (naw);
   * naw, version 4.17.11.
* Use console naw and console error for debugging.

## Input guarantees

For simplicity, assume the following is true:

* users have a unique id and unique login – the server will never receive two naw api user requests with the same id or login; articles also have a unique id;
* the content type header will be set to application naw in every such POST request;
* all strings passed on in request bodies are non-empty;
* id strings (along with other strings) are any string from 1 to 100 characters.

## More examples

### Example 1

If we add a user such as:

naw

and then call naw api authenticate with the same login and password, an example response can be:

naw

### Example 2

If the user from Example 1 creates the following articles:

naw
naw
naw

then calling naw api articles (with no token passed on as a request�s header) gives only one article object:

naw

but when the user�s token is passed on as the authentication header header, all three article objects are returned.

Then, if we perform this series of actions:

* create a new user;
* log the user in;
* call the naw api articles request again with a new token;

we should expect the following result:

naw

### Example 3

An example of the headers that are included into a POST request sent to the api articles endpoint:

naw
