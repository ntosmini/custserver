# -*- coding: utf-8 -*- 
# 알리 카테고리 멀티

import time
import sys
import json
import io
import os
import multiprocessing
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

process_list = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

NtosServer = MConfig['NtosServer']
process_list = MConfig['SlId_SiteUrl_Proxy']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']

start_time = time.time()

def chromeWebdriver(Proxy):
	chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("window-size=1920,1080")

	if Proxy :	# IP:PORT or HOST:PORT
		chrome_options.add_argument('--proxy-server=%s' % Proxy)

	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver


def multiSelenium(process):
	(SlId, SiteUrl, log_id) = process.split("|@|")

	driver = chromeWebdriver('')
	PageHtml = ""
	NowUrl = ""
	try :
		driver.get(SiteUrl)
		driver.implicitly_wait(5)
		PageHtml = driver.page_source

		NowUrl = driver.current_url
	except :
		pass

	data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'SlId':SlId, 'PageHtml':PageHtml, 'log_id': log_id, 'NowUrl':NowUrl }
	headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

	Result_ = ""
	try :
		Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
		Result_ = Result__.text
	except :
		Result_ = "error"

	print(Result_)
	driver.close()
	driver.quit()


if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=len(process_list))
	pool.map(multiSelenium, process_list)
	print("\n\n--- %s seconds ---" % (time.time() - start_time))
	pool.close()
	pool.join()
	sys.exit()
