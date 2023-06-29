# -*- coding: utf-8 -*- 

import time
import sys
import io
import random
import platform
import pc_agent

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.utils import keys_to_typing


#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 파일로 접근
import undetected_chromedriver as uc
from fake_useragent import UserAgent

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

os_info = platform.system()

search_keyword = ['원피스'
,'써스데이아일랜드원피스'
,'블라우스'
,'여름원피스'
,'써스데이아일랜드'
,'롱원피스'
,'여름가디건'
,'남자반바지'
,'티셔츠'
,'반바지'
,'시슬리원피스'
,'라코스테원피스'
,'점프수트'
,'스투시반팔'
,'바스락원피스'
,'플라스틱아일랜드원피스'
,'지고트원피스'
,'쉬폰원피스'
,'린넨원피스'
,'여성원피스'
,'레인부츠'
,'크록스'
,'양산'
,'슬리퍼'
,'샌들'
,'헌터레인부츠'
,'나이키운동화'
,'락피쉬레인부츠'
,'장화'
,'여성샌들'
,'에코백'
,'지비츠'
,'문스타레인부츠'
,'운동화'
,'핏플랍샌들'
,'아쿠아슈즈'
,'크로스백'
,'스케쳐스샌들'
,'캐리어'
,'크록스슬리퍼'
,'선풍기'
,'써큘레이터'
,'제습기'
,'창문형에어컨'
,'냉장고'
,'무선청소기'
,'로봇청소기'
,'에어프라이어'
,'이동식에어컨'
,'미러리스카메라'
,'보조배터리'
,'에어컨'
,'벽걸이에어컨'
,'노트북'
,'모기퇴치기'
,'신일선풍기'
,'포토프린터'
,'앱코키보드'
,'위닉스제습기'
,'청소기'
,'여름이불'
,'행거'
,'쇼파'
,'쿨매트'
,'침대프레임'
,'식탁의자'
,'침대'
,'화장대'
,'매트리스'
,'파티션'
,'암막커튼'
,'앞치마'
,'식탁'
,'서랍장'
,'소파'
,'커튼'
,'선반'
,'책상'
,'전신거울'
,'컴퓨터책상'
,'원터치텐트'
,'수영복'
,'래쉬가드'
,'전기자전거'
,'캠핑의자'
,'파라솔'
,'구명조끼'
,'풋살화'
,'축구화'
,'타프'
,'모노키니'
,'자전거'
,'등산화'
,'골프웨어'
,'텐트'
,'캠핑테이블'
,'비키니'
,'무릎보호대'
,'에어텐트'
,'골프화']

# 크롬드라이버 셋팅
def chromeWebdriver():
		
	chrome_service = ChromeService(ChromeDriverManager().install())
	chrome_options = uc.ChromeOptions()

	agent = pc_agent.get_agent()

	if os_info != 'Darwin' :
		chrome_options.add_argument('--headless=new')

	chrome_options.add_argument('--headless=new')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--blink-settings=imagesEnabled=false')
	chrome_options.add_argument('--window-size=1920,1080')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	chrome_options.add_argument('--disable-infobars')
	chrome_options.add_argument('--disable-setuid-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--user-agent' + agent)

	chrome_options.page_load_strategy = 'normal'

	driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=113)

	return driver

#마우스 휠 움직이기
def MouseScroll(driver) :
	footer = driver.find_element(By.ID, "footer")
	ActionChains(driver).scroll_to_element(footer).perform()

def MouseScroll2(driver) :
	time.sleep(random.uniform(0.5, 5))

	for i in range(0, random.randint(2, 6)) :
		time.sleep(random.uniform(0.2, 1.6))
		ActionChains(driver).scroll_by_amount(0, random.randint(300, 400)).perform()
	
	time.sleep(random.uniform(0.5, 5))


# 키 하나씩 입력해주기
class EnhancedActionChains(ActionChains):
	def send_keys_1by1(self, keys_to_send, time_s=0.2):
		typing = keys_to_typing(keys_to_send)

		for key in typing:
			self.key_down(key)
			self.key_up(key)
			self.w3c_actions.key_action.pause(time_s)

		return self	
	
# 네이버 쇼핑 클릭
def clickShoppingLink(driver) :

	retVal = "success"
	
	try:
		# 네이버 검색 페이지에서 클릭
		elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='https://cr3.shopping.naver.com/v2/bridge/searchGate']")	
		element = elements[random.randint(0, len(elements)-1)]
		ActionChains(driver).move_to_element(element).click().perform()

		time.sleep(random.uniform(0.5, 5))
		driver.switch_to.window(driver.window_handles[1])

		MouseScroll2(driver)
		MouseScroll2(driver)

	except Exception as e:
		retVal = "error"
		print("clickShoppingLink error")
		print(e)
		return retVal

	try:
		# 네이버 쇼핑 페이지에서 클릭
		elements2 = driver.find_elements(By.CSS_SELECTOR, "a[href*='https://cr.shopping.naver.com/adcr.nhn']")	
		element2 = elements2[random.randint(0, len(elements2)-1)]
		ActionChains(driver).move_to_element(element2).click().perform()
		
		time.sleep(random.uniform(0.5, 5))
				
		driver.switch_to.window(driver.window_handles[2])

		MouseScroll2(driver)
		MouseScroll2(driver)
		MouseScroll2(driver)

		driver.close()		
		
		driver.switch_to.window(driver.window_handles[1])

		MouseScroll2(driver)

		driver.close()

	except Exception as e:
		print("clickShoppingLink error2")
		print(e)
		driver.close()
		pass

	return retVal

#네이버 블로그 클릭
def clickBlogLink(driver) :

	retVal = "success"

	try:
		# 네이버 검색 페이지에서 클릭
		elements = driver.find_elements(By.CSS_SELECTOR, "div[class='info_area']>a[href*='https://blog.naver.com/']")	
		element = elements[random.randint(0, len(elements)-1)]
		ActionChains(driver).move_to_element(element).click().perform()

		time.sleep(random.uniform(0.5, 5))

		driver.switch_to.window(driver.window_handles[1])

		MouseScroll2(driver)
		MouseScroll2(driver)
		MouseScroll2(driver)
		MouseScroll2(driver)

		driver.close()
		
	except Exception as e:
		print("clickBlogLink error")
		print(e)
		pass

	
	return retVal
	
	
driver = chromeWebdriver()

driver.delete_all_cookies()

SiteUrl = "https://naver.com"

driver.get(SiteUrl)
driver.implicitly_wait(30) # 처음에만 셋팅

driver.maximize_window()

# 검색창 클릭
elem = driver.find_element(By.XPATH, '//*[@id="query"]')
elem.click()

action = EnhancedActionChains(driver)
action.send_keys_1by1(search_keyword[random.randint(0, len(search_keyword)-1)]).perform()

time.sleep(random.randint(1, 3))

elem.send_keys(Keys.ENTER)

time.sleep(random.randint(1, 3))

MouseScroll2(driver)

time.sleep(random.randint(1, 3))

for i in range(0, random.randint(2, 6)) :

	if random.randint(0, 1) == 0 :
		print(str(i) + "_clickShoppingLink")
		clickShoppingLink(driver)		
	else :
		print(str(i) + "_clickBlogLink")
		clickBlogLink(driver)

	try:
		driver.switch_to.window(driver.window_handles[0])
	except Exception as e:
		print("link click error")
		print(e)
		pass

	time.sleep(random.randint(5, 10))


elem = driver.find_element(By.XPATH, '//*[@id="nx_query"]')
elem.click()
time.sleep(random.uniform(0.2, 1))

if os_info != 'Darwin' :
	elem.send_keys(Keys.CONTROL, "a")
else :
	elem.send_keys(Keys.COMMAND, "a")

time.sleep(random.uniform(0.2, 1))
elem.send_keys(Keys.DELETE)
time.sleep(random.uniform(0.2, 1))

action = EnhancedActionChains(driver)
action.send_keys_1by1("메코틴 본사").perform()

time.sleep(random.randint(1, 3))

elem.send_keys(Keys.ENTER)

print("naver search")

try:

	time.sleep(random.randint(2, 3))

	elements = driver.find_elements(By.XPATH, '//*[@id="main_pack"]/section/div/ul/li')

	print("Before Mecotine Click")
	for elem in elements:
		e = elem.find_element(By.CLASS_NAME, 'total_tit')
		if e.text == "[메코틴] 국내 유일 고품질의 RS-니코틴 메코틴본사":        
			e.click()
			time.sleep(random.randint(1, 2))
			break
	print("After Mecotine Click")

	time.sleep(random.randint(1, 3))

	driver.switch_to.window(driver.window_handles[1])

	time.sleep(random.randint(18, 22))

	num = random.randint(4, 10)

	for i in range(0, num) :
		
		try : 
			print( str(i) + "_before_goods_click")
			a_elements = driver.find_elements(By.CSS_SELECTOR, "li[class='name']>a[href*='shopdetail']")
			a_elements[random.randint(0, len(a_elements)-1)].click()

			del a_elements

			print( str(i) + "_after_goods_click")

			MouseScroll2(driver)
			
			print( str(i) + "_after_goods_click2")

			time.sleep(random.randint(12, 20))
			
			#driver.back()
			driver.execute_script("window.history.go(-1)")

			print( str(i) + "_after_goods_click3")

			time.sleep(random.randint(12, 18))

			print( str(i) + "_end_goods_click")

			
		except Exception as e:
			print( str(i) + "_error_goods_click")
			print(driver.current_url)
			print(e)
			pass

	print("SUCESS")
	driver.quit()

except Exception as e:
	print("예외발생")
	print(e)
	driver.quit()

