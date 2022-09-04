# -*- coding: utf-8 -*- 
import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading
import json
import re
import io

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


SiteUrl = MConfig['SiteUrl']
WebType = MConfig['WebType']
Agent = MConfig['Agent']
Proxy = MConfig['Proxy']
CodeLen = int(MConfig['CodeLen'])


def ScrollDown() :
	SCROLL_PAUSE_SEC = 1
	# 스크롤 높이 가져옴
	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
		# 끝까지 스크롤 다운
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# 1초 대기
		time.sleep(SCROLL_PAUSE_SEC)

		# 스크롤 다운 후 스크롤 높이 다시 가져옴
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height

# "Chrome" or "Firefox" or "curl"
from bs4 import BeautifulSoup
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

if WebType == "curl" :
	from urllib.request import urlopen
	page_html = urlopen(SiteUrl)
	html = BeautifulSoup(page_html, 'html.parser')

	print(html)
	exit()
else :
	from selenium import webdriver
	from selenium.webdriver.common.alert import Alert

	if WebType == "Chrome" :
		#from pyvirtualdisplay import Display
		#display = Display(visible=0, size=(1920, 1080))  
		#display.start()


		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("-disable-notifications")
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument("--window-size=1920x1080")
		if Agent == "" :
			chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
		else :
			chrome_options.add_argument("user-agent="+ Agent)


		driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)


	else :	# 기본 : Firefox
		driver = webdriver.Firefox("/usr/bin/geckodriver")


	#종료
	def DriverQuit():
		driver.close()
		driver.quit()
		exit()

	DriverJob = threading.Timer(120, DriverQuit)
	DriverJob.start()

	driver.get(SiteUrl)
	driver.implicitly_wait(10)
	driver.refresh()
	driver.implicitly_wait(5)
	time.sleep(random.randint(3, 5))
	ScrollDown()

	time.sleep(3)

	DriverJob.cancel()


	page_html = driver.page_source
	ItemList = []

	try :
		ScriptMatched = re.search('\{"mods".*\}', page_html)
		ScriptListData = ScriptMatched.group()

		ScriptListDataArr = json.loads(ScriptListData)
		for Slist in ScriptListDataArr['mods']['itemList']['content'] :
			Code1 = Slist['productId']
			Url = '/item/'+Code1+".html";
			if len(str(Code1)) > CodeLen :
				ItemList.append(str(Code1))
	except :
		pass

	try :
		ItemContentBox = driver.find_element(By.CLASS_NAME, "product-container")
		ATagItems = ItemContentBox.find_elements(By.TAG_NAME, 'a')

		ItemClassName = ''
		for ATI in ATagItems :
			href = ATI.get_attribute('href')
			if re.search("aliexpress.com/item/\d+", str(href)) :
				ItemClassName = href = ATI.get_attribute('class')
				break

		if ItemClassName :
			for ATI2 in ATagItems :
				href = ATI2.get_attribute('href')
				class_ = ATI2.get_attribute('class')
				if class_ == ItemClassName and re.search("aliexpress.com/item/\d+", str(href)) :
					href_result = re.sub(r'(\.html.*)$', '.html', str(href))
					Code2 = re.search("\d+", href_result).group()
					if len(str(Code2)) > CodeLen :
						ItemList.append(str(Code2))
		"""
		ItemContentBox = driver.find_element(By.CLASS_NAME, "product-container")
		#ItemBox = ItemContentBox.find_element(By.XPATH, "div[2]")
		ATagItems = ItemContentBox.find_elements(By.TAG_NAME, 'a')

		for ATI in ATagItems :
			href = ATI.get_attribute('href')
			if re.search("aliexpress.com/item/\d+", str(href)) :
				href_result = re.sub(r'(\.html.*)$', '.html', str(href))
				Code2 = re.search("\d+", href_result).group()
				if len(str(Code2)) > 15 :
					ItemList.append(str(Code2))
		"""
	except :
		pass

	ItemListSet = list(set(ItemList))

	if len(ItemListSet) > 0 :
		for codelist in ItemListSet :
			print(codelist)
	else :
		if ItemContentBox.text :
			print("notitem")
		else :
			print("error")

	driver.close()
	driver.quit()
	exit()
