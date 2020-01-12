import os
import time
from datetime import datetime
import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor

from config import BaseConfig
from models import *
from manage import init_db, connect_db
from clients import SacAjaxScraper, SejongAjaxScraper, LotteAjaxScraper

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


def init_demon():
    init_db(BaseConfig.VIKI_DB_URI)










if __name__ == '__main__':
    from hook import hook
    hook()

#if __name__ == '__main__':
#    init_demon()
