# -*- coding: utf-8 -*- 
# 스크렙

import time
import sys
import json
import io
import os
import requests
import traceback
import random

try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass



#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

SiteUrlArr = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrlArr = MConfig['SiteUrlArr']
FileSaveDir = MConfig['FileSaveDir']
FileSendSave = MConfig['FileSendSave']	#파일 저장 전송 사용여부 y/n
NtosServer = MConfig['NtosServer']	#받을 url

UserAgent = MConfig['UserAgent']
ChromeVer = MConfig['ChromeVer']
headers = ""
if UserAgent :
	headers = {
		"User-Agent":UserAgent
	}
for val in SiteUrlArr :
	(CustId, SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n"

	PageHtml = ""
	NowUrl = ""
	if SiteUrl == "" or SaveFileName == "" :
		pass
	else :
		try :
			if headers :
				PageHtml = requests.get(SiteUrl, headers=headers)
			else :
				PageHtml = requests.get(SiteUrl)
			PageHtml = PageHtml.text
		except :
			PageHtml = str(traceback.format_exc())
		
		WriteFile = "<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
		WriteFile = WriteFile + str(OriginUrl)
		if NowUrl :
			WriteFile = WriteFile + "<ntosnowurl>"+NowUrl+"</ntosnowurl>\n"
		
		WriteFile = WriteFile + PageHtml

		if FileSaveDir :
			SaveFile = FileSaveDir+str(SaveFileName)
			SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
			f = open(SaveFile, 'w', encoding="utf8")
			f.write(WriteFile)
			f.close()
			os.system("gzip "+SaveFile)

			if FileSendSave == "y" and NtosServer != "" :
				gzfile = SaveFile+".gz"
				files = open(gzfile, 'rb')
				upload = {'file': files}
				data = {'CustId':CustId, 'ScrapType':'cate' }
				Result_ = requests.post(NtosServer, data=data, files=upload)
				Result = Result_.text
				if os.path.exists(gzfile) :
					os.remove(gzfile)
		else :
			print(str(WriteFile))
	time.sleep(random.uniform(2, 4))
driver.quit()
