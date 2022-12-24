from os import mkdir
from os.path import exists, expanduser
from yaml import load, CLoader as Loader

def read():
    create_config_file_when_it_does_not_exist()
    config_file = open(get_config_file_path(), 'r').read()
    return load(config_file, Loader=Loader)

def write():
    print("Writing file")

def create_config_file_when_it_does_not_exist():
    config_directory_path = get_config_directory_path()
    if not exists(config_directory_path):
        mkdir(config_directory_path)

    config_file_path = get_config_file_path()
    if not exists(config_file_path):
        open(config_file_path, 'x')

def get_config_directory_path():
    return expanduser('~') + '/.git-with'

def get_config_file_path():
    return get_config_directory_path() + '/config.yaml'