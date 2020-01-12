from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
SCROLL_PAUSE_TIME = 0.5
CONTENTS_LOAD_PAUSE_TIME = 30

drv = webdriver.Chrome('./chromedriver_win32/chromedriver')

drv.get('http://www.sac.or.kr/SacHome/perform/schedule')
drv.execute_script("window.scrollTo(0, 200)")
drv.implicitly_wait(SCROLL_PAUSE_TIME)

# 2월 클릭
drv.find_element_by_xpath('//*[@id="prepared_month_list"]/li[2]').click()
drv.execute_script("window.scrollTo(0, 200)")
drv.implicitly_wait(SCROLL_PAUSE_TIME)

# 전체 탭 클릭
drv.find_element_by_xpath('//*[@id="search_select_gubun"]/li[1]').click()
drv.execute_script("window.scrollTo(0, 200)")
drv.implicitly_wait(SCROLL_PAUSE_TIME)

# 텍스트로 보기 클릭
drv.find_element_by_xpath('//*[@id="txt_list"]').click()
drv.execute_script("window.scrollTo(0, 200)")
drv.implicitly_wait(SCROLL_PAUSE_TIME)

# 공연목록 로드 대기 후 크롤
drv.implicitly_wait(CONTENTS_LOAD_PAUSE_TIME)
dic = {}
idx = 1

while True:
    try:
        xpath = '//*[@id="loaded_list_item_' + str(idx) + '"]/td[1]/a'
        elem = drv.find_element_by_xpath(xpath)
        # TODO: javascript 파일에서 hyperlink 크롤해오기
        hyperlink = None
        dic[str(elem.get_attribute("textContent"))] = hyperlink

        idx += 1
        drv.execute_script("window.scrollTo(0, 200)")
        drv.implicitly_wait(SCROLL_PAUSE_TIME)

    except NoSuchElementException:
        print(xpath)
        print(dic)
        break

print(len(dic))





