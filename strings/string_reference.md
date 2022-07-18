# Strings

## f-string

f-strings can be used to print variables. But it also has some additional formatting stuff.

One way to format numbers in f strings is by including `:,` at the end of the variable name

```text
>>> a = 100000000
>>> print(a)
100000000

>>> print(f'{a:,}')
100,000,000
```
