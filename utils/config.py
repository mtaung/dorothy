import configparser

config_file = 'config.ini'

def load(section:str):
    """Returns a config section with the given name as a dictionary."""
    config = configparser.ConfigParser()
    with open(config_file, 'r') as file: 
        config.read_file(file)
    return config[section]
