The goal of this task is to provide an API with two endpoints: one for creating messages using the POST method and the other for reading a list of them. The reading endpoint should be paginated with cursor-based pagination (for more details take a look at "Hints" section).

### Requirements

The API must contain two endpoints:

#### `POST /messages`

1.   This endpoint will create a message stored in the local SQLite DB by calling provided `saveMessage` function. Each created message will receive an incrmental `id` field from the database.
2.   The payload body of this request will look like this:

    ```json
    {
        "date": "2019-11-11",
        "author": "John",
        "channel": "general",
        "text": "Hi there"
    }
    ```

3.   The request will return a successful response with status code `201` and no payload.
4.   If any of the properties is missing, the service should instead return a `422` status code.

#### `GET /messages`

1.   If no query parameters are specified, this endpoint will return all messages sorted by internal DB index (propert `id`), in descending order. The default count of records will be 10.
2.   The client may provide the following query parameters:

  2.1.   `count` (number) specifies the number of returned messages (default: 10);
  2.2.   `next` specifies a cursor pointing to the next record for the given request (default: first records should be returned);
        -   Clients should take `next` cursor from the payload of one of the requests (see payload below `paging.next`)
        -   Calling `GET /messages` with a `next` cursor will give the issuer the next data for the given query. e.g. given messages A, B, C, D, first request with `count` 2 returned messages D, C and a `next` cursor. Sending second request with this `next` value and `count` 2 should returns the next 2 records: B and A.
        -   If there is nothing to show in the `next` cursor then the `next` property must be set to the empty string.
        -   Adding new message should not result in any shifting or duplication of records while paging.
            For example, say the request `GET /messages` has a total of 100 messages. Initially, the first 10 are returned with a cursor for messages 11-20. If a new message is then added, the query with a cursor must still return the messages that were previously in places 11-20, even though they are actually 12-21 now.

3.   Example payload of a response looks like this:

    ```json
    {
        "data": [
            {
                "date": "2019-11-12",
                "author": "John",
                "channel": "general",
                "text": "Hi hi"
            },
            {
                "date": "2019-11-11",
                "author": "John",
                "channel": "random",
                "text": "Hi there!"
            }
        ],
        "paging": {
            "next": "MTMzNw=="
        }
    }
    ```

4.   Sorting by `id` should result in the newest messages being shown first. So if client adds messages A, B, C, D (in that order) then by requesting `GET /messages?count=2` they should get messages D and C.

### Hints

1.   You can store data in a cursor in any way you want as long as the endpoint behaves as required. This might be just an `id` of the last record or encoded structure.
2.   Common approach is to use `id`s from DB and filter the records that contain only higher/lower `id`. This is possible when the `id` is set by the database incrementally.
3.   Relying on internal "indexing" (`id` field) of the data to ensures that adding new messages will not "break" the cursor.
4.   The task uses following versions of dependencies:

```json
{
    "dependencies": {
        "body-parser": "1.19.0",
        "express": "4.17.1"
    }
}
```

### Examples

The endpoints are expected to behave as follows:

  1.   assuming that following messages exist in the system:

        ```json
        [
            {
                "id": 1,
                "channel": "general",
                "author": "Jane",
                "text": "Hi there!",
                "date": "2020-01-01"
            },
            {
                "id": 2,
                "channel": "general",
                "author": "John",
                "text": "Hello Jane!",
                "date": "2020-01-01"
            },
            {
                "id": 3,
                "channel": "general",
                "author": "Jane",
                "text": "How are is it going?",
                "date": "2020-01-01"
            }
        ]
        ```

  2.   sending request to `GET /messages?count=2` would result in response:

        ```json
        {
            "data": [
                {
                    "id": 3,
                    "channel": "general",
                    "author": "Jane",
                    "text": "How is it going?",
                    "date": "2020-01-01"
                },
                {
                    "id": 2,
                    "channel": "general",
                    "author": "John",
                    "text": "Hello Jane!",
                    "date": "2020-01-01"
                }
            ],
            "paging": {
                "next": "xyz" // the content on "next" is irrelevant it might be just "3" or something else
            }
        }
        ```

  3.   given this response to get next part of the data user should request `GET /messages?count=2&next=xyz` which would result in response:
        ```json
        {
            "data": [
                {
                    "id": 1,
                    "channel": "general",
                    "author": "Jane",
                    "text": "Hi there!",
                    "date": "2020-01-01"
                }
            ],
            "paging": {
                "next": ""
            }
        }
        ```
