"""
Run this with something like this
`argparse_example.py --message hahaha --blah "what even is this"`
"""
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", type=str)
parser.add_argument("-b", "--blah", type=str)

# Don't pass in anything for this one
# The reference for this will be something_something
parser.add_argument(
    "-s", "--something-something", default="default something something", type=str
)

args = parser.parse_args()
print(f"This is the argument that was received: {args.message}")
print(f"This is the value of blah: {args.blah}")
print(f"This is the value of something something: {args.something_something}")
