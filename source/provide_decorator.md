[Decorators](https://wiki.python.org/moin/PythonDecorators) are one of the most powerful tools that can be used by Python programmers. A decorator can change a decorated class or function, e.g. to validate arguments, inject an argument or register a function somewhere (functools.singledispatch/pytest.fixture). Argument injection could be leveraged to make functions shorter: instead of burdening them with the explicit creation of required resources, one could just write a decorator to inject a handle to a temporary file or database connection.

### Requirements

Write a decorator that satisfies the following requirements:
1. The decorator should provide the decorated function with all keyword arguments passed to the decorator (see example 1).
2. The decorator should preserve the function's positional arguments and their order (see examples 2 and 3).
3. The decorator should leave the possibility to explicitly pass the arguments to a decorated function (see example 4).
4. The decorated function should retain the same name, docstring and other features that it had before it was decorated.
5. In a case where the decorated function does not accept an argument with a given name, and does not use `**kwargs`, ignore that argument and do not pass it (see example 5).


### Examples

1. A simple example of how a decorator is used on a function - illustrating requirement 1:
```python
@provide(a=2)
def add(a: int, b: int) -> int:
    return a + b
add(b=3)  # 5, because expression @provide(a=2) injected `a`
```

2. Example of how the decorator should preserve the order of the positional arguments of the decorated function - illustrating requirement 2:
```python
@provide(a=2)
def add(a: int, b: int) -> int:
    return a + b
# add(3)  # this would not work - the order of positional arguments is preserved,
          # so `add` thinks it is receiving `a` twice
```

3. Another example of how the decorator should preserve the positional arguments of the decorated function - illustrating requirement 2:
```python
# If we provide `b`...
@provide(b=2)
def add(a: int, b: int) -> int:
    return a + b
add(3)  # 5, we are still able to use `a` as a positional argument
```

4. Example of leaving open the possibility to explicitly pass the arguments to a decorated function - illustrating requirement 3:
```python
@provide(a=2)
def add(a: int, b: int) -> int:
    return a + b
add(3, 4)  # 7, despite function `add` being decorated, we have explicitly specified `a`
add(a=3, b=4)  # 7, this is equivalent
```

5. Example of how the decorator ignores arguments that are not defined in a function that does not accept `**kwargs` - illustrating requirement 5:
```python
@provide(nonexistent=123, b=1)
def add(a: int, b: int) -> int:
    return a + b
add(4)  # returns 5, `nonexistent` is ignored
```
