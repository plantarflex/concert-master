import os
import time
from datetime import datetime
import multiprocessing
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor

from config import Config
from models import *
from logger import Logger
from manage import init_db, connect_db
from clients import Sac, Sejong, Lotte, AjaxScraper

from sqlalchemy.orm import sessionmaker


def init_demon():
    init_db(Config.VIKI_DB_URI)
    global logger
    logger = Logger()


def scrape(sc, thread_name):
    logger.create(thread_name, levels=['DEBUG', 'INFO', 'ERROR'])
    postgres_engine = connect_db(Config.VIKI_DB_URI)
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


def hook(thread_idx, lock):
    while True:
        print('online')
        time.sleep(10)


def run():
    lock = Lock()
    with ThreadPoolExecutor(max_workers=Config.THREAD_WORKERS_NUM) as executor:
        for idx in range(1, Config.THREAD_WORKERS_NUM+1):
            executor.submit(
                hook,
                idx,
                lock
                )


def run_accordingly():
    thread_1 = Thread(target=thread_work, args=(1,))
    thread_1.start()
    thread_1.join()

if __name__ == '__main__':
    try:
        init_demon()
    except Exception as e:
        print('>>>>>>>> Demon initiation error')
    else:
        run()
