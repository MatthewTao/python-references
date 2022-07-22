# PyTest

Usage of PyTest in general and how to play around with the references.

## How to use reference

Change directory to the `pytest` in `python-references`.
From there, the various commands can then be run.

To run all the tests present:

> python -m pytest

To run tests in just one file:

> python -m pytest tests/unit/test_datetime_utils.py

Run tests by node ids: Each collected test is assigned a unique node-id which consist of the module filename followed by specifiers like class names, function names and parameters from parametrization, separated by :: characters.

To run a specific test within a module:

> python -m pytest tests/unit/test_datetime_utils.py::test_combine_date_and_time

Another example (which doesn't work for this reference) specifying a test method in the command line:

> python -m pytest test_mod.py::TestClass::test_method

There are also options that can be passed in to pytest, here are some common ones:

- `-v` for verbose
- `--maxfail=num` to keep on testing even if some tests fail
- `--ignore=path` to ignore some paths from the test discovery, can include multiple times

So for example:

> python -m pytest -v --maxfail=10
