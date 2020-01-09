from scraper.sac_ajax_scraper import SacAjaxScraper
from scraper.sejong_ajax_scraper import SejongAjaxScraper
from scraper.lotte_ajax_scraper import LotteAjaxScraper
import json
import os
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
    sac_tester = Tester(SacAjaxScraper, 2019, 11)
    sac_tester.run_test()
    print(
        sac_tester.result
    )

    print('********** sejong **********')
    sejong_tester = Tester(SejongAjaxScraper, 2019, 11)
    sejong_tester.run_test()
    print(
        sejong_tester.result
    )

    print('********** lotte **********')
    lotte_tester = Tester(LotteAjaxScraper, 2017)
    lotte_tester.run_test()
    print(
        lotte_tester.result
    )


    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(BASE_DIR, '../json_files/sac.json'), 'w+') as sac_file:
        json.dump(sac_tester.result, sac_file)

    with open(os.path.join(BASE_DIR, '../json_files/sejong.json'), 'w+') as sejong_file:
        json.dump(sac_tester.result, sejong_file)

    with open(os.path.join(BASE_DIR, '../json_files/lotte.json'), 'w+') as lotte_file:
        json.dump(sac_tester.result, lotte_file)
