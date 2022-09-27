# Python dataclasses

Python dataclasses are a good way to encapsulate data in an object.
It's simple to define and simple to read and retrieve.

It is only available in Python 3.7+

## Example dataclass

A data class just needs to have the `@dataclass` decorator

```python
from dataclass import dataclass


@dataclass
class Person:
    name: str
    address: str
    active: bool = True
```

Can include most of the things like type hinting, setting defaults, and stuff

## More detailed example

There are also quite a few options that can be applied to data classes as well.

- the class can be turned into an immutable object with `frozen=True`
- properties can be taken off the input with `init=False`
- properties can be removed from the print with `repr=False`
- properties can be generated after init with `__post_init__`

```python
from dataclass import dataclass


def generate_uuid():
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass(frozen=True)
class Person:
    name: str
    address: str
    active: bool = True
    uuid: str = field(init=False, default_factory=generate_uuid)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f'{self.name} {self.address}'
```

If we are using 3.10+, there are additional features as well.

`slots=True` in the decorator makes accessing the properties much faster.
But slots cannot be used with dataclasses that inherit from another dataclass.
That being said, dataclass with inheritance probably would lead to tight coupling
and therefore should be avoided.
