import yaml

def get_config():
    """
    Load the configuration settings from a YAML file.
    """
    with open('config/settings.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config
