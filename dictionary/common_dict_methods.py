"""
Some common methods that might be done for dictionaries
"""

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


def iterate_over_keys_and_values(dictionary):
    for key, value in dictionary.items():
        print(f"This is one of the keys {key} and it's value: {value}")
        # Note it is bad practice to modify the object that is being iterated.
        # Create another object to hold the results if needed.
