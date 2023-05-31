# -*- coding: utf-8 -*- 
import time
import sys
import io
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 파일로 접근
import undetected_chromedriver as uc
from fake_useragent import UserAgent

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def chromeWebdriver():

    ua = UserAgent()
    chrome_service = ChromeService(ChromeDriverManager().install())
    chrome_options = Options()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled') # 이걸로도 되네?
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--user-agent=' + ua.random)
    chrome_options.page_load_strategy = 'normal'
    driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=113)

    return driver

driver = chromeWebdriver()

driver.delete_all_cookies()

SiteUrl = "https://naver.com"

driver.get(SiteUrl)
driver.implicitly_wait(10) # 처음에만 셋팅

driver.maximize_window()

# 검색창 클릭
elem = driver.find_element(By.XPATH, '//*[@id="query"]')
time.sleep(random.randint(1, 2))
elem.click()
elem.send_keys("메")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("코")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("틴")
time.sleep(random.uniform(1, 2))
elem.send_keys(Keys.ENTER)

try:

    time.sleep(random.randint(2, 3))

    elements = driver.find_elements(By.CLASS_NAME, "api_more_wrap")

    for elem in elements:
        e = elem.find_element(By.TAG_NAME, 'a')
        if e.text == "검색결과 더보기":
            e.click()
            time.sleep(random.randint(1, 2))
            break

    time.sleep(random.randint(3, 6))

except:
    print("EXCEPT")


for i in range(2,4):
        
    # 해당 엘레멘트가 있는지 확인
    try:
        elm = driver.find_elements(By.CSS_SELECTOR, "a[href='http://pf.kakao.com/_tqxhxfxj']")

        if len(elm) == 0:
            # 엘레멘트가 없으면 페이지 이동
            page_elm = driver.find_element(By.CLASS_NAME, "sc_page_inner")
            pe = page_elm.find_elements(By.TAG_NAME, 'a')
            pe[i].click()
            time.sleep(random.randint(4, 6))
            continue
        else :            
            elm[random.randint(1, len(elm)-1)].click()
            time.sleep(random.randint(9, 15))
            break
        
    except NoSuchElementException:
        print("PAGE FALSE")
        pass

print("SUCCESS")

driver.quit()