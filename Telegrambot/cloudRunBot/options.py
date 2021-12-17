import yaml
from os import environ


def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def get_options(config_filename) -> dict:
    return read_yaml(config_filename)
