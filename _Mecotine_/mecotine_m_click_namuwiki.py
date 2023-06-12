# -*- coding: utf-8 -*- 

import time
import sys
import io
import random


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys


#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# pip3 으로 설치
import undetected_chromedriver as uc 

# 파일로 접근
#import undetected_chromedriver as uc
from fake_useragent import UserAgent

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import undetected_chromedriver as uc 

def chromeWebdriver():

	chrome_service = ChromeService(ChromeDriverManager().install())
	chrome_options = uc.ChromeOptions()

	chrome_options.add_argument('--headless=new')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--blink-settings=imagesEnabled=false')
	chrome_options.add_argument('--window-size=1920,1080')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	chrome_options.add_argument('--disable-infobars')
	chrome_options.add_argument('--disable-setuid-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')    
	chrome_options.page_load_strategy = 'normal'
	driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=113)

	return driver


driver = chromeWebdriver()

driver.delete_all_cookies()


SiteUrl = "https://m.naver.com"


driver.get(SiteUrl)
driver.implicitly_wait(10) # 처음에만 셋팅

driver.maximize_window()

time.sleep(random.randint(1, 3))

# 모바일인 경우
driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]').click()


# 검색창 클릭
elem = driver.find_element(By.XPATH, '//*[@id="query"]')
elem.click()
elem.send_keys("메")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("코")
time.sleep(random.uniform(0.1, 1))
elem.send_keys("틴")
time.sleep(random.uniform(1, 2))
elem.send_keys(Keys.ENTER)

try:

	time.sleep(random.uniform(5, 10))

	elm = driver.find_elements(By.CSS_SELECTOR, "a[href='https://namu.wiki/w/%EB%A9%94%EC%BD%94%ED%8B%B4']")

	if len(elm) == 0:
		print("NOT URL")
		driver.quit()
		exit
	else :            
		elm[random.randint(1, len(elm)-1)].click()
		time.sleep(random.randint(9, 15))
	

	a_elements = driver.find_elements(By.TAG_NAME, "a")
	for a_elem in a_elements:
		if "mecotine.com" in a_elem.get_attribute("href"):
			a_elem.click()
			break

	time.sleep(random.randint(10, 20))

	driver.switch_to.window(driver.window_handles[-1])

	time.sleep(random.randint(18, 22))

	a_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='shopdetail']")

	a_elements[random.randint(0, len(a_elements)-1)].click()

	time.sleep(random.randint(9, 12))

except:
	print("EXCEPT")
	driver.quit()


print("SUCCESS")
driver.quit()