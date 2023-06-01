# -*- coding: utf-8 -*- 

import time
import sys
#import json
import io
#import os
#import re
import random
#import traceback


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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
	chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	chrome_options.add_argument('--disable-infobars')
	#chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
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
elem.click()
elem.send_keys("메")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("코")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("틴")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("본")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("사")
time.sleep(random.uniform(1, 2))
elem.send_keys(Keys.ENTER)

try:

    time.sleep(random.randint(2, 3))

    elements = driver.find_elements(By.XPATH, '//*[@id="main_pack"]/section/div/ul/li')

    for elem in elements:
        e = elem.find_element(By.CLASS_NAME, 'total_tit')
        if e.text == "[메코틴] 국내 유일 고품질의 RS-니코틴 메코틴본사":        
            e.click()
            time.sleep(random.randint(1, 2))
            break

    time.sleep(random.randint(1, 3))

    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(random.randint(18, 22))

    a_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='shopdetail']")

    a_elements[random.randint(0, len(a_elements)-1)].click()

    time.sleep(random.randint(9, 12))

    print("SUCCESS")

except:
    print("EXCEPT")

# 종료
driver.quit();
