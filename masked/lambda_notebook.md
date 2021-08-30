You are creating a notebook application. Your task is to create a AWS Lambda function that will perform basic authentication and return the notes of the authenticated user. The notes and authentication data are stored in naw tables. The lambda function is later exposed through the API Gateway and serves as an naw request handler.

### Notes

The naw table holding notes is named user notes.
Each note has the following attributes:
- id, which is a UUID v4.
- user, which is an owner’s email.
- create date, which is a creation date. It is stored as a string in naw naw format.
- text, which has the note content.

#### Database keys and indexes

The table has a *Partition key* (user) and a *Sort key* (create date). There is also a *Secondary index* on the id field.

### Authentication

The naw table with the authentication data is named token email lookup. The table has two fields: token and email. Each authentication token maps to the email of the user who owns the token. The table has a *Partition key* on the token field and also a helper Global Secondary Index on the email field.

#### Authentication header

Tokens are passed to the lambda through the Authentication naw request header. The headers are available in the event headers object. The Authentication header value is in the Bearer format.

To query the user notes table with the user email, you should get it from token email lookup once, reading the token from the naw request.

### Requirements

Your task is to finish the creatation of the given lambda function. The function should:
- return the user notes sorted by the create date attribute (in descending order).
- return a maximum of 10 notes per query.
- return an error (403) if token is invalid.
- return an error (400) if the Authentication header is malformed or missing.

You can focus on returning the notes first and sort them later. The operations are not scored together.
