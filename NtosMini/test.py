# -*- coding: utf-8 -*- 
#!/usr/bin/python3
import time
import sys
import codecs

import base64

SiteUrl = sys.argv[1]
SiteUrl = base64.b64decode(SiteUrl).decode()


from selenium import webdriver

from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")


driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

if SiteUrl == "not" :
	driver.get('http://ntos.co.kr')
else :
	driver.get(SiteUrl)

	#경고창
	try :
		result = driver.switch_to_alert()
#		result.accept()
		result.dismiss()
	except :
		pass


if 'amazoan.' in SiteUrl :
	# 배송지 위치
	element = driver.find_element_by_xpath('//*[@id="glow-ingress-line2"]')
	nation = element.text

	if nation.capitalize() == "carlstadt 07072‌" :
		pass
	else :
		element.click()
		time.sleep(3)
		#zip code 넣는 부분에 키를 넣고 apply 버튼을 클릭해준다.
		zipcode = driver.find_element_by_xpath('//*[@id="GLUXZipUpdateInput"]')
		zipcode.send_keys('07072')
		time.sleep(0.5)
		driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input').click()
		time.sleep(2)

		#이후 버튼이 여러개 나올 수 있어서 element가 존재하는 버튼 클릭 이벤트 주기.


try {
		$driver->findElement(WebDriverBy::xpath('//*[@id="a-popover-3"]/div/div[2]/span/span/span/button'))->click();
	} catch(Exception $e) {
		echo "Error 1";
	}
	try {
		$driver->findElement(WebDriverBy::xpath('/html/body/div[6]/div/div/div[2]/span/span/input'))->click();
	} catch(Exception $e) {
		echo "Error 2";
	}
	try {
		$driver->findElement(WebDriverBy::xpath('//*[@id="GLUXConfirmClose"]'))->click();
	} catch(Exception $e) {
		echo "Error 3";
	}


		try :
			driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/span/span/span/button').click()
		except :
			pass

		try :
			driver.find_element_by_xpath('//*[@id="a-popover-1"]/div/div[2]/span/span/span/button').click()
		except :
			pass

		try :
			driver.find_element_by_xpath('//*[@id="a-popover-2"]/div/div[2]/span/span/span/button').click()
		except :
			pass

		try :
			driver.find_element_by_xpath('//*[@id="a-popover-3"]/div/div[2]/span/span/span/button').click()
		except :
			pass

		try :
			driver.find_element_by_xpath('//*[@id="a-popover-4"]/div/div[2]/span/span/span/button').click()
		except :
			pass

		try :
			driver.find_element_by_xpath('//*[@id="a-popover-5"]/div/div[2]/span/span/span/button').click()
		except :
			pass
else :
	pass


time.sleep(3)
page_html = driver.page_source
driver.quit()
	
html = BeautifulSoup(page_html, 'html.parser')
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())
print(html)