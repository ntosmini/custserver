# -*- coding: utf-8 -*- 
# 카테고리 멀티-v4

import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading
import json
import re
import io
import os
import multiprocessing
import requests
import traceback
#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

process_list = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


NtosServer = MConfig['NtosServer']
process_list = MConfig['CslId_SiteUrl']
Agent = MConfig['Agent']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
Scroll = MConfig['Scroll']
Refresh = MConfig['Refresh']
TimeChk = MConfig['TimeChk']
Referer = MConfig['Referer']

if TimeChk == "Y" :
	start_time = time.time()

executable_path = ChromeDriverManager().install()

def chromeWebdriver():
	chrome_service = ChromeService(executable_path)
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument("--blink-settings=imagesEnabled=false")
	chrome_options.add_argument("window-size=1920,1080")

	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver

def multiSelenium(process):
	print(process)

if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=len(process_list))
	pool.map(multiSelenium, process_list)
	if TimeChk == "Y" :
		print("\n\n--- %s seconds ---" % (time.time() - start_time))
	pool.close()
	pool.join()
	sys.exit()
