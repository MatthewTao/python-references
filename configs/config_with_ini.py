import configparser


config = configparser.ConfigParser()
config.read("config.ini")
print(config)
print(config["DEFAULT"])
for line in config["DEFAULT"]:
    print(f"The key of the config: {line}")
    print(f'The value of the config: {config["DEFAULT"][line]}\n')
