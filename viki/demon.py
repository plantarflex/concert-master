import os
import time
from datetime import datetime
import multiprocessing
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from config import BaseConfig
from models import *
from manage import init_db, connect_db
from clients import Sac, Sejong, Lotte, AjaxScraper

from sqlalchemy.orm import sessionmaker


def init_demon():
    init_db(BaseConfig.VIKI_DB_URI)


def Scrape(sc):
    postgres_engine = connect_db(BaseConfig.VIKI_DB_URI)
    Session = sessionmaker(bind=postgres_engine)
    while True:
        time.sleep(10)
        session = Session()
        s_time = datetime.now()
        ## TODO: how much to scrape...?
        scraper = AjaxScraper(sc, s_tme.year, s_time.month)
        for perform in scraper.scrape():
            old_perform = session.\
                query(Perform).\
                filter(Perform.name == perform['name']).\
                first()
            if old_perform is not None:
                session.close()
                continue
            ## TODO: convert date to datetime
            new_perform = Perform(**perform)
            session.add(new_perform)
        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()







if __name__ == '__main__':
    from hook import hook
    hook()

#if __name__ == '__main__':
#    init_demon()
