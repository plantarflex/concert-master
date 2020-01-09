import requests


def date_to_sting(year, month):
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    year = str(year)
    return year, month


class SacAjaxScraper:
    def __init__(self, year, month):
        year, month = date_to_sting(year, month)
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
        payload = self.getPerformList_request
        response = requests.post(
                url='http://www.sac.or.kr/SacHome/perform/getPerformList',
                json=payload,
                headers={
                    'X-Requested-With': 'XMLHttpRequest',
                }
            )
        self.perform_list = response.json()
        self.response_status_code = response.status_code

    def parse_to_schema(self):
        lst = []
        for perform in self.perform_list:
            d = {}
            d['startDate'] = int(perform['startDate'].replace('.', ''))
            d['endDate'] = int(perform['endDate'].replace('.', ''))
            d['programName'] = perform['programName']
            d['placeName'] = perform['placeName']
            d['priceInfo'] = perform['priceInfo']
            d['hyperLink'] = 'http://www.sac.or.kr/SacHome/perform/detail?searchSeq=' + str(perform['seq'])
            lst.append(d)
        return lst