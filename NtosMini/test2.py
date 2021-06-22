# -*- coding: utf-8 -*- 

# 모니터 해상도 : 1920 * 1080
import time
import sys
import codecs
import requests
#pip install pyperclip	클립
import pyperclip

#pip install pyautogui	키보드
import pyautogui  

from tkinter import Tk


"""
from selenium.webdriver.common.keys import Keys

elem = find_element_by_name("our_element")
elem.send_keys("bar")
elem.send_keys(Keys.CONTROL, 'a') #highlight all in box
elem.send_keys(Keys.CONTROL, 'c') #copy
elem.send_keys(Keys.CONTROL, 'v') #paste
"""
from bs4 import BeautifulSoup
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.alert import Alert

#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(1920, 1080))  
#display.start()

chrome_options = webdriver.ChromeOptions()


chrome_options.add_argument('window-size=1920,1080')
"""
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920x1080")
"""
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

driver = webdriver.Chrome("C:/xampp/htdocs/_Ntos/_Trans/chromedriver.exe", chrome_options=chrome_options)
#driver = webdriver.Chrome("C:/xampp/htdocs/_Ntos/_Trans/chromedriver.exe")

time.sleep(1)
actions = ActionChains(driver)
#actions.key_down(Keys.ALT).send_keys('x').key_up(Keys.ALT).perform()

driver.get("https://papago.naver.com/?sk=en&tk=ko")

time.sleep(1)

#내용 가져오기
"""
f = open("C:/xampp/htdocs/_Ntos/_Trans/_TransOne_namelist.txt", "r", encoding="utf8")
itemname = f.read()
f.close()
"""

from urllib.request import urlopen


page_html = urlopen(SiteUrl)
html = BeautifulSoup(page_html, 'html.parser')
html = str(html)

(itemcode,itemname) = html.split("@|@")


pyperclip.copy(itemname)




#driver.find_element_by_xpath('/html/body/div/div/div[2]/section/div/div[1]/div[1]/div/div[3]/label/textarea').click()
time.sleep(3)
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

actions = ActionChains(driver)
pyperclip.copy('')
time.sleep(3)
##actions.key_down(Keys.TAB).key_up(Keys.TAB).perform()


"""
actions.move_by_offset(0, 0).click().perform()

time.sleep(1)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(1)
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
#actions.move_by_offset(0, 0).context_click().perform()	#우클릭
"""
driver.find_element_by_xpath('/html/body/div/div/div[2]/section/div/div[1]/div[2]/div/div[7]/span[2]/span/span/button').click()



#result = Tk().selection_get(selection="CLIPBOARD")
result = pyperclip.paste()

driver.quit()

print(itemcode+" = "+result)
exit()




time.sleep(1)
URL = 'http://amazon.ntos.co.kr/_Mini_/_WinTrans/ItemWinTransSe.php' 
data = {'CustId': 'amazon', 'mode': 'up', 'TransType':'papagose', 'codelist':itemcode, 'namelist' : result } 
response = requests.post(URL, data=data)


"""
time.sleep(3)
actions = ActionChains(driver)
actions.send_key(Keys.F6).perform()






time.sleep(3)
pyautogui.hotkey('alt', 'space')
time.sleep(1)
pyautogui.hotkey('x')
time.sleep(1)
"""
