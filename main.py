import configparser

config = configparser.ConfigParser()
config.read('src/config.ini')
print(config['DEFAULT']['Compression'])     # -> "/path/name/"


























