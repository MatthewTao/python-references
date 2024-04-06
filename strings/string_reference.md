# Strings

## f-string

f-strings can be used to print variables. But it also has some additional formatting stuff.

One way to format numbers in f strings is by including `:,` at the end of the variable name

``` text
>>> a = 100000000
>>> print(a)
100000000

>>> print(f'{a:,}')
100,000,000
```

To control the number of decimals displayed of a float

``` python
pi = 3.141592
print(f"{pi:.2f}")
# 3.14
```

To display floats as percentages

``` python
value = 0.5
print(f"{value:0%}")
# 50%

print(f"{value:1%}")
# 50.0%
```

To display something in scientific notation

``` python
value = 12345678910
print(f"{value:e}")
# 1.2345678910e+10

print(f"{value:.2e}")
# 1.23E+10
```

To display date and datetime objects as strings

``` python
datetime_obj = datetime(
    year=2024,
    month=2,
    day=13,
)
print(f"{datetime_obj:%Y-%m-%d}")
# 2024-02-13
```
