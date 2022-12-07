# -*- coding: utf-8 -*- 
# 테스트

import time
import sys
import json
import io
import os
import multiprocessing
import requests
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrl = MConfig['SiteUrl']
RefreshUsed = MConfig['refresh']
LogUsed = MConfig['log']

start_time = time.time()


logfile = "/var/log/nginx/scrap_log_"+time.strftime('%Y%m%d', time.localtime(time.time()))+".txt"

def logsave(text) :
	if LogUsed == "n" :
		return
	filechk = ''
	logdata = ''
	if os.path.isfile(logfile) :
		f = open(logfile, 'r', encoding="utf8")
		logdata = f.read()
		f.close()
		filechk = 'y'
	else :
		filechk = 'n'
	
	if text :
		val = ""
		chktime = str( round((time.time() - start_time), 2))
		if text == "start" :
			val = "============================= start "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			
		elif text == "end" :
			val = "\n============================= end "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+" >> "+chktime+" seconds \n\n\n"
		else :
			val = "\n"+str(text)+" "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+" >> "+chktime+" seconds "
		
		f = open(logfile, 'w', encoding="utf8")
		f.write(str(logdata)+str(val))
		f.close()


logsave("start")
logsave("ChromeService 체크전")
executable_path = ChromeDriverManager().install()
logsave("ChromeService 체크완료")

def chromeWebdriver():
	chrome_service = ChromeService(executable_path)
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("window-size=1920,1080")
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver

logsave("chromeWebdriver 실행전")
driver = chromeWebdriver()
logsave("chromeWebdriver 실행완료")
try :
	logsave("chromeWebdriver 이동전"+str(SiteUrl))
	driver.get(SiteUrl)
	driver.implicitly_wait(10)
	logsave("chromeWebdriver 이동완료"+str(SiteUrl))
	if RefreshUsed == "y" :
		logsave("refresh 전")
		driver.refresh()
		driver.implicitly_wait(10)
		logsave("refresh 완료")
	logsave("source 불러오기전")
	page_html = driver.page_source
	logsave("source 불러오기 완료")
	print(page_html)
	driver.close()
	driver.quit()
except :
	err = traceback.format_exc()
	logsave("try except")+str(err)
	print(str(err))
	driver.close()
	driver.quit()
	
logsave("end")
