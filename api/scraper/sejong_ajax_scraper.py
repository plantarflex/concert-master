import requests
from bs4 import BeautifulSoup as BS


def date_to_sting(year, month):
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    year = str(year)
    return year, month


class SejongAjaxScraper:
    def __init__(self, year, month):
        year, month = date_to_sting(year, month)
        self.getPerformList_request = "langCode=001" \
                                      "&currentYear=" + year + \
                                      "&currentMonth=" + month + \
                                      "&currentDay=" \
                                      "&sval=" \
                                      "&currPage=1" \
                                      "&performIdx=" \
                                      "&performCode=" \
                                      "&listType=2" \
                                      "&bcode=" \
                                      "&placeCode=" \
                                      "&genreCode=" \
                                      "&artGroupCode=" \
                                      "&menuNum=0101" \
                                      "&searchGubun=MONTH"
        self.perform_list = None
        self.response_status_code = None

    def scrape_perform_list(self):
        payload = self.getPerformList_request
        response = requests.post(
                url='http://www.sejongpac.or.kr/controls/ajax/performanceList.asp',
                data=payload,
                headers={
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            )
        soup = BS(response.content, features='lxml')
        self.perform_list = soup.table.tbody.find_all('tr')
        self.response_status_code = response.status_code

    def parse_to_schema(self):
        lst = []
        for perform in self.perform_list:
            d = {}
            info = perform.find_all('td')
            schedule = perform.find('span').contents
            href_info_list = perform.a['href'].lstrip('javascript:goView(').rstrip(');').split(', ')
            d['startDate'] = int(schedule[0][:-2].replace('.', ''))
            d['endDate'] = int(schedule[2])
            d['programName'] = perform.a.contents[0]
            d['placeName'] = info[2].contents[0]
            d['priceInfo'] = None
            d['hyperLink'] = 'http://www.sejongpac.or.kr/performance/view_real.asp?performIdx=' \
                             + href_info_list[0].strip("'") + '&performCode=' + href_info_list[2].strip("'")
            lst.append(d)
        return lst