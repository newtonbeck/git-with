from os import mkdir
from os.path import exists, expanduser
from yaml import load, dump, CLoader as Loader

def introduce(alias, name, email):
    config = read()

    new_user = {
        'alias': alias,
        'name': name,
        'email': email
    }
    
    current_users_without_new_user = list(filter(lambda user: user['alias'] != alias, config['users']))
    current_users_without_new_user.append(new_user)

    config['users'] = current_users_without_new_user

    write(config)
    

def read():
    create_config_file_when_it_does_not_exist()
    config_file = open(get_config_file_path(), 'r').read()
    return load(config_file, Loader=Loader)

def write(config):
    with open(get_config_file_path(), 'w') as out_file:
        dump(config, out_file, default_flow_style=False)

def create_config_file_when_it_does_not_exist():
    config_directory_path = get_config_directory_path()
    if not exists(config_directory_path):
        mkdir(config_directory_path)

    config_file_path = get_config_file_path()
    if not exists(config_file_path):
        base_config = {
                'users': [],
                'current_session': []
            }
        write(base_config)

def get_config_directory_path():
    return expanduser('~') + '/.git-with'

def get_config_file_path():
    return get_config_directory_path() + '/config.yaml'