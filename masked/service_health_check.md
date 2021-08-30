Health-checking is a name for making sure that a given network service is responsive and alive. This approach is used for issues detection, warnings about failures or even automated restarts. The task here is to create a function that will check the status of few net services. Each of those services has an endpoint  status that can be queried against using naw protocol. There is no service that uses HTTPS - every one uses plain naw.

Create a function that performs health checking for a given list of service addresses. A service address is a string with a valid domain name with port, for example localhost:8000. You can use the following libraries:
* naw naw
* naw naw

A service is considered to be healthy if it responds to a health check request in no longer than 0.5 second and naw code will be equal to 200 OK. If service does not respond within 0.5 second or naw code of response is not 200 OK, the service is considered unhealthy. Requests should be sent using GET method.

The function is expected to return a dictionary where service address (as given in the argument) is a key and value is either True if service is healthy or False otherwise.

Example with a single address:
naw

Example with more than one address:
naw

Example of using naw library:
naw
