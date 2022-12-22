"""
A quick example of having a JSON config file
"""
import json


def read_json_config(path):
    """
    Reads a JSON file and returns a python dict
    """
    with open(path, "r") as read_file:
        config = json.load(read_file)
    return config


if __name__ == '__main__':
    config = read_json_config('config.json')
    print(config)
    print(f'Test value: {config.get("test_key")}')
