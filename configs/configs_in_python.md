# Configs in Python

Configurations are important to get right.
A particularly important feature of configurations is that
it will enable testing of the code in different environments.
Each environment will hit and use different infrastructure and use different secrets.
It also means that the application or product can be flexibly changed.

The common ways a config file is created now is using one of the following formats:

- YAML
- JSON
- TOML
- INI

The file should be

- Easy to read and edit for anyone
- easy to deploy
- ideally can include comments
- ideally also doesn't need to depend on a third party library

## INI Files

INI files are text based and are easy to edit and read,
supports comments,
and doesn't need a third party library to use.

But the downside is that everything is encoded as string.

## YAML Files

YAML files are text based,
easy to edit and read,
and supports comments.
It supports some typing like booleans and dictionaries.

## JSON Files

Very similar to YAML files in terms of pros, but doesn't support comments.

## TOML Files

Similar to INI files but can be messy when the structure gets a bit too complicated.

## Third party config solutions

Aside from writing configurations to files, there are some other libraries that handle config.
For example `dynaconf` or `hydra`.
These will wrap around one of the file types anyway but bring some extra functionality as well.
Probably not the best for simplicity,
but would be better for larger and more complex configurations.
