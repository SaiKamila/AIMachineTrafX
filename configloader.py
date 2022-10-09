import configparser

config = configparser.ConfigParser()
config.read('resources/appconfig.properties')

def load_config():
    return config