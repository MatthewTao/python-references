"""
Run this with something like this
`argparse_example.py --message hahaha --blah "what even is this"`
"""
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    '-m',
    '--message',
    type=str
)
parser.add_argument(
    '-b',
    '--blah',
    type=str
)

args = parser.parse_args()
print(f'This is the argument that was received: {args.message}')
print(f"This is the value of blah: {args.blah}")
