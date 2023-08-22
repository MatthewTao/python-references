# Match statements

In python 3.10, `match` statements were introduced.
They fill in the role of switch statements quite well.
They have the rough syntax as below:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:  # `or` keyword can be used instead
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
```

This can be used to replace ladder if else blocks that we used to use,
or using dictionaries to map the cases.
