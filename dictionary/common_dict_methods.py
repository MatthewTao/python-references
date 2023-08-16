"""
Some common methods that might be done for dictionaries
"""
from operator import itemgetter

# This also contains a simple example of dictionary comprehension.
def sort_dictionary(dictionary):
    """
    This sorts a dictionary based on the key.
    Quite basic, probably wouldn't be suitable for large dictionaries.
    """
    keys = list(dictionary.keys())
    keys.sort()
    
    sorted_dictionary = {key: dictionary[key] for key in keys}

    return sorted_dictionary


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
    for key, value in dictionary.items():
        print(f"This is one of the keys {key} and it's value: {value}")
        # Note it is bad practice to modify the object that is being iterated.
        # Create another object to hold the results if needed.


if __name__ == '__main__':
    list_of_dicts = [
        {"col1": 2, 'unrelated': 'hahaha'},
        {"col1": 6, 'idk': 2},
        {"col1": 3, 'something else': 3}
    ]
    print(sort_list_of_dictionaries_v2(list_of_dicts, 'col1'))
