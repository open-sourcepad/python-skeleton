import os
import configparser
from itertools import chain


BRAND_NAME = 'Falcon REST API Template'
UUID_LEN = 10
UUID_ALPHABET = ''.join(map(chr, range(48, 58)))
TOKEN_EXPIRES = 3600

INI_FILE = os.path.abspath(os.path.abspath(os.path.join('conf/config.ini')))
CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

APP_SETTINGS = CONFIG['app_settings']
DATABASE = CONFIG['database']
DB_CONN_STRING = "{type}://{username}:{password}@{host}:{port}/{db_name}".format(
    type=DATABASE['type'],
    username=DATABASE['username'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port'],
    db_name=DATABASE['db_name'],
)

DATABASE_TEST = CONFIG['database_test']
DB_TEST_CONN_STRING = "{type}://{username}:{password}@{host}:{port}/{db_name}".format(
    type=DATABASE_TEST['type'],
    username=DATABASE_TEST['username'],
    password=DATABASE_TEST['password'],
    host=DATABASE_TEST['host'],
    port=DATABASE_TEST['port'],
    db_name=DATABASE_TEST['db_name'],
)

METHOD_DEFAULTS = {
    'index': { 'methods': ['GET'] },
    'show': { 'methods': ['GET'] },
    'create': { 'methods': ['POST'] },
    'update': { 'methods': ['PUT', 'PATCH'] },
    'delete': { 'methods': ['DELETE'] },
}
