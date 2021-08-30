Decorators naw are one of the most powerful tools that can be used by naw programmers. A decorator can change a decorated class or function. For example, to validate arguments, inject an argument or register a function somewhere (functools.singledispatch pytest.fixture). Argument injection can be used to make functions shorter. Instead of creating each required resource explicitly, one can write a decorator to inject a handle to a temporary file or database connection.

### Requirements

Write a decorator that meets the following requirements:
The decorator should provide the decorated function with all keyword arguments passed to the decorator (see example 1).
The decorator should keep the function’s positional arguments and their order (see examples 2 and 3).
The decorator should leave the possibility to explicitly pass the arguments to a decorated function (see example 4).
The decorated function should keep the same name, docstring and other features that it had before it was decorated.
If the decorated function does not accept an argument with a given name, and does not use naw, do not pass it (see example 5).


### Examples

A simple example of how a decorator is used on a function - example for requirement 1:
naw

Example of how the decorator should keep the order of the positional arguments of the decorated function - example for requirement 2:
naw

Another example of how the decorator should keep the positional arguments of the decorated function - example for requirement 2:
naw

Example of leaving open the possibility to explicitly pass the arguments to a decorated function - example for requirement 3:
naw

Example of how the decorator does not pass arguments that are not defined in a function that does not accept naw - example for requirement 5:
naw
