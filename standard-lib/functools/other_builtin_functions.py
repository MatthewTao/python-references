"""
Not strictly a functools method but seems quite useful for functions in general
"""


def simple_map_example():
    def myfunc(n) -> int:
        return len(n)

    results = map(myfunc, ('apple', 'banana', 'cherry'))
    for result in results:
        print(result)

    x, y = map(int, ["1", "2"])
    assert x == 1
    assert y == 2


def more_parameters_example():
    """
    The function just needs to have the same number of parameters as the number of iterables
    """
    def other_function(a, b):
        return a + b

    c, d = map(other_function, [1, 2], [3, 4])
    assert c == 4
    assert d == 6


def simple_filter():
    people = [{"name": "Bob", "age": 12}, {"name": "Carl", "age": 21}, {"name": "Dyson", "age": 19}]

    def over_eighteen(person):
        age = person.get("age")
        return age > 18
    over_eighteens = filter(over_eighteen, people)
    assert len(list(over_eighteens)) == 2
    for item in over_eighteens:
        assert item["age"] > 18

    # After iterating over filter result, the instances are removed
    assert len(list(over_eighteens)) == 0


if __name__ == "__main__":
    simple_map_example()
    more_parameters_example()
    simple_filter()
