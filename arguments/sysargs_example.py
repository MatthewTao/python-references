"""
Run this example with something like this
`python sysargs_example.py hahaha`
"""
import sys


name_of_script = sys.argv[0]
first_arg = sys.argv[1]

print(f"script called was: {name_of_script}")
print(f"First arg provided was: {first_arg}")
