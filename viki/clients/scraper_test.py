import json
import os

from Sac import SacAjaxScraper
from Sejong import SejongAjaxScraper
from Lotte import LotteAjaxScraper

from bs4 import BeautifulSoup as BS


class Tester:
    def __init__(self, scraper, year, month=None):
        self.scraper = scraper(year, month)
        self.result = None

    def run_test(self):
        self.scraper.scrape_perform_list()
        self.result = self.scraper.parse_to_schema()


if __name__ == '__main__':
    print('********** sac **********')
    sac_tester = Tester(SacAjaxScraper, 2020, 1)
    sac_tester.run_test()
    print(
        sac_tester.result
    )

#    print('********** sejong **********')
#    sejong_tester = Tester(SejongAjaxScraper, 2019, 11)
#    sejong_tester.run_test()
#    print(
#        sejong_tester.result
#    )

    print('********** lotte **********')
    lotte_tester = Tester(LotteAjaxScraper, 2017)
    lotte_tester.run_test()
    print(
        lotte_tester.result
    )
