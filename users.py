from os import mkdir
from os.path import exists, expanduser
from yaml import load, dump, CLoader as Loader

def introduce(alias, name, email):
    config = __read()

    new_user = {
        'alias': alias,
        'name': name,
        'email': email
    }
    
    current_users_without_new_user = list(filter(lambda user: user['alias'] != alias, config['users']))
    current_users_without_new_user.append(new_user)

    config['users'] = current_users_without_new_user

    __write(config)

def add(aliases):
    config = __read()

    aliases_already_introduced = list(map(lambda user: user['alias'], config['users']))
    aliases_to_be_added = list(filter(lambda alias: alias in aliases_already_introduced, aliases))

    config['current_session'] = list(set(config['current_session'] + aliases_to_be_added))

    __write(config)
    
    return aliases_to_be_added

def remove(aliases):
    config = __read()

    current_session = set(config['current_session'])

    aliases_that_will_be_removed = set(current_session.intersection(set(aliases)))
    
    config['current_session'] = list(current_session - aliases_that_will_be_removed)

    __write(config)

    return list(aliases_that_will_be_removed)

def reset_current_session():
    config = __read()

    aliases_that_will_be_removed = config['current_session']

    config['current_session'] = []

    __write(config)

    return aliases_that_will_be_removed

def get_users_in_current_session():
    config = __read()

    current_session = config['current_session']
    all_users = config['users']

    users_in_current_session = list(filter(lambda user: user['alias'] in current_session, all_users))

    return users_in_current_session


def __read():
    __create_config_file_when_it_does_not_exist()
    config_file = open(__get_config_file_path(), 'r').read()
    return load(config_file, Loader=Loader)

def __write(config):
    with open(__get_config_file_path(), 'w') as out_file:
        dump(config, out_file, default_flow_style=False)

def __create_config_file_when_it_does_not_exist():
    config_directory_path = __get_config_directory_path()
    if not exists(config_directory_path):
        mkdir(config_directory_path)

    config_file_path = __get_config_file_path()
    if not exists(config_file_path):
        base_config = {
                'users': [],
                'current_session': []
            }
        __write(base_config)

def __get_config_directory_path():
    return expanduser('~') + '/.git-with'

def __get_config_file_path():
    return __get_config_directory_path() + '/config.yaml'