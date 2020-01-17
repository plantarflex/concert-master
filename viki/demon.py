import os
import time
from datetime import datetime
import multiprocessing
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from config import BaseConfig
from models import *
from log import Logger
from manage import init_db, connect_db
from clients import Sac, Sejong, Lotte, AjaxScraper

from sqlalchemy.orm import sessionmaker


def init_demon():
    init_db(BaseConfig.VIKI_DB_URI)
    global logger
    logger = Logger()


def scrape(sc, thread_name):
    logger.create(thread_name, levels=['DEBUG', 'INFO', 'ERROR'])
    postgres_engine = connect_db(BaseConfig.VIKI_DB_URI)
    Session = sessionmaker(bind=postgres_engine)
    while True:
        time.sleep(10)
        session = Session()
        s_time = datetime.now()
        # TODO: how much to scrape...?
        scraper = AjaxScraper(sc, s_tme.year, s_time.month)
        for perform in scraper.scrape():
            old_perform = session.\
                query(Perform).\
                filter(Perform.name == perform['name']).\
                first()
            if old_perform is not None:
                #TODO: how to see if it is updated...?
                logger[thread_name].info('perform already exists')
                continue
            ## TODO: convert date to datetime
            new_perform = Perform(**perform)
            session.add(new_perform)
            try:
                session.commit()
            except Exception as e:
                print(e)
                session.rollback()
                continue


def scrape_concurrently():
    scrapers = {
        'sac': Sac, 'sejong': Sejong, 'lotte': Lotte
    }
    with ThreadPoolExecutor as executor:
        for k,v in scrapers.items():
            executor.submit(k,v)
    

if __name__ == '__main__':
    from hook import hook
    hook()

#if __name__ == '__main__':
#    init_demon()
