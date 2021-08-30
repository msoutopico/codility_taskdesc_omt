You are writing an endpoint that returns the total number of items bought in your online store by a given user.
Orders in your system are stored in an external service called `OrdersService`. Your task is to:
- write an endpoint in the given `UsersController` class;
- write a method in the given `UsersService` class that counts the number of items bought by the given user;
- configure the `UsersController` and `UsersService` classes.

Solving this task requires from you editing the following three files. Please make sure they are all present in your final solution.
- `com.codility.app.AppConfiguration`
- `com.codility.app.UsersController`
- `com.codility.app.UsersService`

#### Interfaces

The `UsersService` class declares:
- a field `ordersService`: `private OrdersService ordersService`
- a method `getNumberOfItemsBought`: `public int getNumberOfItemsBought(String username)`

The `UsersController` class declares:
- a field `usersService`: `private UsersService usersService`
- a method `totalItemsBought`: `public Map<String, Integer> totalItemsBought()`

They are all present in your initial solution.

#### Environment
Your application is written with the Spring Framework.

Your Spring context is already populated with the `OrdersService` bean that implements the following interface:
```
package com.codility.external;

import java.util.List;

public interface OrdersService {

    List<Item> itemsBought(String username);

}
```
Note that `OrdersService` is located in the `com.codility.external` package, whereas your application uses the `com.codility.app` package.

### Requirements
1. Make sure that the `AppConfiguration` class is treated as a Spring configuration bean.

2. Configure Spring to scan for beans in the `com.codility.external` package.

3. Prepare the `OrdersService` bean (please refer to the signatures described above):
    - Inject the `OrdersService` bean into the `ordersService` field.
    - Use it in the `getNumberOfItemsBought` method to count the number of items bought by the given user.

4. Inject `UsersService` into `UsersController`.

5. Use it in the `totalItemsBought` method to fetch the number of items bought by the given user.

6. The `totalItemsBought` method should implement the following contract:
    - endpoint URL: `/users/{username}/items/total`, where `username` is a path variable;
    - response JSON format: `{"totalItemsBought":number}`, where `number` is the number of items bought by the given user;
    - status code 200 in case of a successful response.

7. Make sure you pass the `username` variable to the `totalItemsBought` call.

8. For simplicity, you don't have to write any input validation or error handling.

9. You are working with the Spring Framework version 5.1.7 and Java 8.
