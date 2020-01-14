import requests



class SacAjaxScraper:
    def __init__(self, year, month):
        self.getPerformList_request = {
            "languageCd": "K",
            "limitMaxNo": "",
            "searchSeq": "",
            "searchPlaceCd": "1004",
            "searchStartDt": year + month + "01",
            "searchEndDt": year + month + "31",
            "sort": "",
            "startIndex": 1,
            "endIndex": 100
        }
        self.perform_list = None
        self.response_status_code = None

    def scrape_perform_list(self):
        response = requests.post(
                url='http://www.sac.or.kr/SacHome/perform/getPerformList',
                json=self.getPerformList_request,
                headers={
                    'X-Requested-With': 'XMLHttpRequest',
                })
        self.response_status_code = response.status_code
        self.perform_list = response.json()

    def parse_to_schema(self):
        lst = []
        if self.response_status_code != 200:
            print('scrape request failed')
            return lst
        for perform in self.perform_list:
            d = {}
            d['start_date'] = int(perform['startDate'].replace('.', ''))
            d['end_date'] = int(perform['endDate'].replace('.', ''))
            d['name'] = perform['programName']
            d['house'] = 'sac'
            d['hall'] = perform['placeName']
            d['price_info'] = perform['priceInfo']
            d['link'] = 'http://www.sac.or.kr/SacHome/perform/detail?searchSeq=' + str(perform['seq'])
            lst.append(d)
        return lst

