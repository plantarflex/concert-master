import json
import os

from Sac import SacAjaxScraper
from Sejong import SejongAjaxScraper
from Lotte import LotteAjaxScraper


class Tester:
    def __init__(self, scraper, year, month=None):
        self.scraper = scraper(str(year), str(month))
        self.result = None

    def run_test(self):
        self.scraper.scrape_perform_list(),
        self.scraper.parse_to_schema()
        return (
            self.scraper.perform_list,
            self.scraper.response_status_code,
            type(self.scraper.response_status_code)
            )


if __name__ == '__main__':
    print('********** sac **********')
    sac_tester = Tester(SacAjaxScraper, 2020, 1)
    print(sac_tester.run_test())

#    print('********** sejong **********')
#    sejong_tester = Tester(SejongAjaxScraper, 2019, 11)
#    sejong_tester.run_test()
#    print(
#        sejong_tester.result
#    )

#    print('********** lotte **********')
#    lotte_tester = Tester(LotteAjaxScraper, 2017)
#    lotte_tester.run_test()
#    print(
#        lotte_tester.result
#    )
