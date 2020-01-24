import requests


class LotteAjaxScraper:     # 연 단위로 통째로 긁어오는 방법이 최선
    def __init__(self, year, month=None):
        self.getPerformList_request = "year=" + year + \
                                      "&month=1" \
                                      "&day=1" \
                                      "&pageIndex="
        self.perform_list = []
        self.response_status_code = None

    def scrape_perform_list(self, page_index):
        response = requests.post(
            url='http://www.lotteconcerthall.com/kor/Performance/IndexConcerts',
            data=self.getPerformList_request + str(page_index),
            headers={
                'Content-Length': '35',   #TODO: content-length chunk 시켜 omit 할 수 있는 방법 권장됨
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest'
                }
            )
        self.perform_list += response.json()['concerts']  # this is list
        has_next_page = response.json()['pager']['HasNextPage']
        if has_next_page is True:           # 해당년도 이후로 계속 검색하게 됨
            page_index += 1
            self.scrape_perform_list(page_index=page_index)

        self.response_status_code = response.status_code

    def parse_to_schema(self):
        lst = []
        for perform in self.perform_list:
            d = {}
            schedule = perform['englishPlaySchedule'][:-6].replace('.', '')
            d['startDate'] = int(schedule)
            d['endDate'] = int(schedule)
            d['programName'] = perform['title']
            d['placeName'] = perform['place']
            d['priceInfo'] = perform['price']
            d['hyperLink'] = 'http://www.lotteconcerthall.com/kor/Performance/ConcertDetails/' \
                             + str(perform['id'])
            lst.append(d)
        return lst
