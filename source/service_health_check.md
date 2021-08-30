Health-checking is a name for ensuring that given network service is responsive & alive. This approach is used for issues detection, warnings about failures or even automated restarts. The task here is to implement a function that will be checking status of few net services. Each of those services has an endpoint /status that can be queried against using HTTP protocol. There is no service that utilizes HTTPS - every one uses plain HTTP.

Implement a function that is to perform health checking for a given list of service addresses. The latter is a string with a valid domain name with port, e.g. localhost:8000. You can use the following libraries:
* [asyncio](https://docs.python.org/3/library/asyncio.html)
* [aiohttp](http://docs.aiohttp.org/en/stable/client_quickstart.html)

A service is considered to be healthy if it responds to a health check request in no longer than 0.5 second and HTTP code will be equal to 200 OK. In case service fails to respond within 0.5 second or HTTP code of response is not 200 OK, the service is to be considered unhealthy. Requests should be sent using GET method.

The function is expected to return a dictionary where service address (as given in the argument) is a key and value is either True if service is healthy or False otherwise.

Example with a single address:
```python
result = await health_check(['localhost:8000'])
print(result)  # {'localhost:8000': True}
```

Example with multiple addresses:
```python
result = await health_check(['localhost:8080', 'intrepid:9000', 'enterprise:8008'])
print(result)  # {'localhost:8080': True, 'intrepid:9000': False, 'enterprise:8008': True}
```

Example of using aiohttp library:
```python
import aiohttp

async with aiohttp.ClientSession() as session:
    # it is possible to test it outside the Codility UI
    # by setting the url to eg. http://httpbin.org/get
    # in the Codility UI all external network access is restricted
    async with session.get('http://localhost:8080') as resp:
        print(resp.status)  # prints HTTP status as integer
        print(await resp.text())  # prints response body as text
```
