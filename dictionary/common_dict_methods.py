"""
Some common methods that might be done for dictionaries
"""
from operator import itemgetter


# This also contains a simple example of dictionary comprehension.
def sort_dictionary_by_keys(dictionary):
    """
    This sorts a dictionary based on the key.
    Quite basic, probably wouldn't be suitable for large dictionaries.
    """
    keys = list(dictionary.keys())
    keys.sort()

    sorted_dictionary = {key: dictionary[key] for key in keys}

    return sorted_dictionary


def sort_dictionary_by_values(dictionary):
    """
    This sorts a dictionary based on the value
    """
    return {
        key: value
        for key, value in sorted(dictionary.items(), key=lambda item: item[1])
    }


def sort_list_of_dictionaries(dicts, key, reverse=False):
    """
    This sorts a list of dictionaries based on the value of a specified key
    """
    sorted_list = sorted(dicts, key=lambda d: d[key], reverse=reverse)
    return sorted_list


def sort_list_of_dictionaries_v2(dicts, key, reverse=False):
    """
    This sorts a list of dictionaries based on the value of a specified key

    Uses itemgetter from operator
    """
    sorted_list = sorted(dicts, key=itemgetter(key), reverse=reverse)
    return sorted_list


def iterate_over_keys_and_values(dictionary):
    """
    This does a FIFO iteration.
    Well at least in Python 3.6+
    Otherwise random order
    """
    for key, value in dictionary.items():
        print(f"This is one of the keys {key} and it's value: {value}")
        # Note it is bad practice to modify the object that is being iterated.
        # Create another object to hold the results if needed.


def destructively_iterate_over_keys_and_values(dictionary: dict):
    """
    This does a LIFO iteration
    """
    while dictionary:
        key, value = dictionary.popitem()
        print(f"This is one of the keys {key} and it's value: {value}")


if __name__ == "__main__":
    incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
    sorted_incomes = sort_dictionary_by_values(incomes)
    print(sorted_incomes)

    list_of_dicts = [
        {"col1": 2, "unrelated": "hahaha"},
        {"col1": 6, "idk": 2},
        {"col1": 3, "something else": 3},
    ]
    print(sort_list_of_dictionaries_v2(list_of_dicts, "col1"))
