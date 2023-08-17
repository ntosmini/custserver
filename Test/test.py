# -*- coding: utf-8 -*- 

from selenium import webdriver as wd
import chromedriver_autoinstaller
import time
import traceback
PageHtml = 'no'
try :
	path = chromedriver_autoinstaller.install()
	driver = wd.Chrome(path)
	driver.get("http://ntos.co.kr")
	driver.implicitly_wait(10)
	PageHtml = driver.page_source
except :
	print(str(traceback.format_exc()))
print(PageHtml)
driver.close()
driver.quit()
