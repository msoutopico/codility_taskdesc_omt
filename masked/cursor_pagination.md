The goal of this task is to provide an API with two endpoints: one for creating messages using the POST method and the other for reading a list of them. The reading endpoint should be paginated with cursor-based pagination (for more details take a look at Hints section).

### Requirements

The API must contain two endpoints:

#### naw messages

1. This endpoint will create a message stored in the local SQLite DB by calling provided save Message function. Each created message will receive an incremental id field from the database.
2. The payload body of this request will look like this:

    naw

3. The request will return a successful response with status code 201 and no payload.
4. If any of the properties is missing, the service should instead return a 422 status code.

#### naw messages

1. If no query parameters are specified, this endpoint will return all messages sorted by internal DB index (propert id), in descending order. The default count of records will be 10.
2. The client may provide the following query parameters:

2.1.   count (number) specifies the number of returned messages (default: 10);
2.2.   next specifies a cursor pointing to the next record for the given request (default: first records should be returned);
-   Clients should take next cursor from the payload of one of the requests (see payload below paging naw)
-   Calling naw messages with a next cursor will give the issuer the next data for the given query. For example, given messages A, B, C, D, you should first request with count 2 returned messages D, C and a next cursor. Sending a second request with this next value and count 2 should return the next 2 records: B and A.
-   If there is nothing to show in the next cursor then the next property must be set to the empty string.
-   Adding a new message should not result in any shifting or duplication of records while paging.
For example, say the request naw messages has a total of 100 messages. To start with, the first 10 are returned with a cursor for messages 11-20. If a new message is then added, the query with a cursor must still return the messages that were previously in places 11-20, even though they are actually 12-21 now.

3. Example payload of a response looks like this:

    naw

4. Sorting by id should result in the newest messages being shown first. So if a client adds messages A, B, C, D (in that order) then by requesting naw messages  count = 2 they should get messages D and C.

### Hints

1. You can store data in a cursor in any way you want as long as the endpoint behaves as required. This might be just an id of the last record or encoded structure.
2. A common approach is to use ids from DB and filter the records that contain only higher lower id. This is possible when the id is set by the database incrementally.
3. Rely on internal indexing (id field) of the data to make sure that adding new messages will not break the cursor.
4. The task uses the following versions of dependencies:

naw

### Examples

The endpoints are expected to behave as follows:

1. assuming that following messages exist in the system:

   naw

2. sending a request to naw messages  count = 2 would result in response:

   naw

3. given this response, to get the next part of the data, the user should request naw messages  count = 2  next = xyz which would result in response:
   naw
