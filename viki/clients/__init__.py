from .Lotte import LotteAjaxScraper as Lotte
from .Sac import SacAjaxScraper as Sac
from .Sejong import SejongAjaxScraper as Sejong


class AjaxScraper:
    def __init__(self, scraper, year, month):
        year = str(year)
        month = '0' + str(month) if month < 10 else str(month)
        self.scraper = scraper(year, month)

    def scrape(self, *args, **kwargs):
        self.scraper.scrape_perform_list(*argsi, **kwargs)
        return self.scraper.parse_to_schema(*args, **kwargs)
