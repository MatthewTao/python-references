# Python Lambda

Lambdas are a pretty standard addition to functional languages.
common along with functions like `map()`, `filter()`, and `reduce()`.
This quote from the Python Design and History FAQ seems to set the tone
about the overall expectation regarding the usage of lambda functions in Python:

> Unlike lambda forms in other languages, where they add functionality,
> Python lambdas are only a shorthand notation if you’re too lazy to define a function.
> <https://docs.python.org/3/faq/design.html#why-can-t-lambda-expressions-contain-statements>

The simplest example of a lambda might look like the below,
which is equivalent to what is further below.

```python
lambda x: x
```

```python
def identity(x):  
    return x
```

both of them takes an argument x and returns it upon invocation.

Because a lambda function is an expression, it can be named. Therefore, you could write the previous code as follows:

```python
>>> add_one = lambda x: x + 1
>>> add_one(2)
3
```

The above lambda function is equivalent to writing this:

```python
def add_one(x):
    return x + 1
```

## Appendix

This is mainly a summary of <https://realpython.com/python-lambda/>
