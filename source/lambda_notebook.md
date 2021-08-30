You are creating a notebook application. Your task is to implement the AWS Lambda function that will perform basic authentication and return the notes of the authenticated user. The notes and authentication data are stored in DynamoDB tables. The lambda function is later exposed through the API Gateway and serves as an HTTP request handler.

### Notes

The DynamoDB table holding notes is named `user-notes`.
Each note has the following attributes:
- `id`, which is a UUID v4;
- `user`, which is an owner’s `email`;
- `create_date`, which is a creation date, stored as a string in [ISO_8601](https://en.wikipedia.org/wiki/ISO_8601) format;
- `text`, which holds actual note content.

#### Database keys and indexes

The table consists of a *Partition key* (`user`) and a *Sort key* (`create_date`). Additionally, there is a *Secondary index* on the `id` field.

### Authentication

The DynamoDB table holding the authentication data is named `token-email-lookup`. The table has two fields: `token` and `email`. Each authentication token maps to the email of the user owning the given token. The table has a *Partition key* on the `token field` and also a helper `GlobalSecondaryIndex` on the `email` field.

#### Authentication header

Tokens are passed to the lambda through the `Authentication` HTTP request header. The headers are available in the `event.headers` object. The `Authentication` header value takes the `Bearer <TOKEN>` format.

To query the `user-notes` table with the user email, you should get it from `token-email-lookup` once, reading the token from the HTTP request.

### Requirements

Your task is to finish the implementation of the given lambda function. The function should:
- return the user notes sorted by the `create_date` attribute (in descending order),
- return a maximum of 10 notes per query,
- return an error (status 403) if `token` is invalid,
- return an error (status 400) if the `Authentication` header is malformed or missing.

You can focus on returning the notes first and sort them later; the operations are scored separately.
