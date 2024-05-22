"""
Example of reading from a yaml config file
"""
import yaml


def read_yaml_config():
    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)

    return config


if __name__ == "__main__":
    test_config = read_yaml_config()
    print(test_config)
    print(f'Config is now a dict: {test_config.get("high_level_heading_1")}')
    print(f'Config is now a dict: {test_config["high_level_heading_1"]["key1"]}')
    print(f'Config at the root level: {test_config["root_level_item"]}')
