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
