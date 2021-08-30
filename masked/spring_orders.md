You are writing an endpoint that returns the total number of items bought in your online store by a given user.
Orders in your system are stored in an external service called Orders Service. We ask you to:
- write an endpoint in the given Users Controller class.
- write a method in the given Users Service class that counts the number of items bought by the given user.
- configure the Users Controller and Users Service classes.

Solving this requires you edit the following three files. Please make sure they are all present in your final solution.
- naw app App Configuration
- naw app Users Controller
- naw app Users Service

#### Interfaces

The Users Service class declares:
- a field orders Service: Orders Service orders Service.
- a method get Number Of Items Bought: int get Number Of Items Bought String username.

The Users Controller class declares:
- a field users Service: Users Service users Service.
- a method total Items Bought: Map total Items Bought.

They are all present in your initial solution.

#### Environment
Your application is written with the Spring Framework.

Your Spring context already has the Orders Service bean that uses the following interface:
naw
Note that Orders Service is in the naw external package, while your application uses the com naw naw package.

### Requirements
Make sure that the App Configuration class is treated as a Spring configuration bean.

Configure Spring to scan for beans in the naw external package.

Prepare the Orders Service bean (please see the signatures described above):
   - Inject the Orders Service bean into the orders Service field.
   - Use it in the get Number Of Items Bought method to count the number of items bought by the given user.

Inject Users Service into Users Controller.

Use it in the total Items Bought method to fetch the number of items bought by the given user.

The total Items Bought method should have the following contract:
   - endpoint URL: users username items total, where username is a path variable.
   - response naw format: total Items Bought number, where number is the number of items bought by the given user.
   - status code 200 in case of a successful response.

Make sure you pass the username variable to the total Items Bought call.

You don’t have to write any input validation or error handling.

You are working with the Spring Framework version 5.1.7 and naw 8.
