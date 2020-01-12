import sys, os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pathlib import Path


basedir = os.path.dirname(s.path.abspath(__file__))
env_path = Path(os.path.join(basedir, '..')) / '.env'
load_dotenv(dotenv_path=env_path)


def is_linux_system():
    return sys.platform == "linux" or sys.platform == "linux2"


class BaseConfig:
    VIKI_DB_NAME = os.environ['VIKI_DB_NAME']
    VIKI_DB_USER = os.environ['VIKI_DB_USER']
    VIKI_DB_PASS = os.environ['VIKI_DB_PASS']
    VIKI_DB_SERVICE = os.environ['VIKI_DB_SERVICE']
    VIKI_DB_PORT = os.environ['VIKI_DB_PORT']
    VIKI_DB_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        VIKI_DB_USER, VIKI_DB_PASS, VIKI_DB_SERVICE, VIKI_DB_PORT, VIKI_DB_NAME)
    SQLALCHEMY_BINDS = {'viki': VIKI_DB_URI }

## TODO: TBA...
#    VIEWER_DB_NAME = os.environ['VIEWER_DB_NAME']
#    VIEWER_DB_USER = os.environ['VIEWER_DB_USER']
#    VIEWER_DB_PASS = os.environ['VIEWER_DB_PASS']
#    VIEWER_DB_SERVICE = os.environ['VIEWER_DB_SERVICE']
#    VIEWER_DB_PORT = os.environ['VIEWER_DB_PORT']
#    VIEWER_DB_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
#        VIEWER_DB_USER, VIEWER_DB_PASS, VIEWER_DB_SERVICE, VIEWER_DB_PORT, VIEWER_DB_NAME)
#    SQLALCHEMY_DATABASE_URI = VIEWER_DB_URI #FIXME

