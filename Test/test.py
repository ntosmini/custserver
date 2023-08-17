# -*- coding: utf-8 -*- 

from selenium import webdriver 

import chromedriver_autoinstaller
import traceback
PageHtml = 'no'
try :
	chromedriver_autoinstaller.install()
	driver = webdriver.Chrome()
	driver.get("http://ntos.co.kr")
	driver.implicitly_wait(10)
	PageHtml = driver.page_source
except :
	print(str(traceback.format_exc()))
print(PageHtml)
driver.close()
driver.quit()
