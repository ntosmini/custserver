from selenium import webdriver as wd
import chromedriver_autoinstaller
import time

path = chromedriver_autoinstaller.install()

driver = wd.Chrome(path)

driver.get("http://ntos.co.kr")

driver.implicitly_wait(10)
PageHtml = driver.page_source
print(PageHtml)
driver.close()
driver.quit()
