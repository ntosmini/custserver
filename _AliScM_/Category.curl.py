# -*- coding: utf-8 -*- 
#알리 카테고리 모바일 curl

import time
import sys
import json
import io
import os
import random
import requests
import traceback
import re

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

SiteUrlList = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrlList = MConfig['SiteUrlList']
CustId = MConfig['CustId']
FileSendSave = MConfig['FileSendSave']  #저장후 전송여부
NtosServer = MConfig['NtosServer']  #전송서버 url
FileDir = MConfig['FileDir']  #저장폴더
CookiesLang = MConfig['CookiesLang']	#언어 및 통화 (ko | en)

cookies_en = {
'xman_us_f': 'x_l=0&x_locale=en_US&x_c_chg=1&acs_rt=',
'aep_usuc_f': 'site=usa&c_tp=USD&region=US&b_locale=en_US',
'intl_locale': 'en_US',
}
cookies_ko = {
'xman_us_f': 'x_l=0&x_locale=ko_KR&x_c_chg=1&acs_rt=',
'aep_usuc_f': 'site=kor&c_tp=KRW&region=KR&b_locale=ko_KR',
'intl_locale': 'ko_KR',
}

sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
import _agent
UserAgent = _agent.get_mobile_agent()

headers = {
	"User-Agent":UserAgent
}

for val in SiteUrlList :
	#에러msg
	ErrMsg = ''
	PageHtml = ''
	(SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n\n"
	#저장파일명
	SaveFile = FileDir+str(SaveFileName)
	SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
	if SiteUrl == "" or SaveFileName == "" :
		pass
	else :
		try :
			if CookiesLang == "ko" :
				PageHtml = requests.get(SiteUrl, headers=headers, cookies=cookies_ko)
			elif CookiesLang == "en" :
				PageHtml = requests.get(SiteUrl, headers=headers, cookies=cookies_en)
			else :
				PageHtml = requests.get(SiteUrl, headers=headers)
			PageHtmlRecode = PageHtml.status_code
			PageHtml = PageHtml.text
		except :
			PageHtml = ''
			PageHtmlRecode = 'error'
			ErrMsg = str(traceback.format_exc())+"\n\n"
		print(ErrMsg)
		WriteFile = "<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
		WriteFile = WriteFile + OriginUrl + PageHtml + ErrMsg

		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		os.system("gzip "+SaveFile)

		if FileSendSave == "Y" and NtosServer != "" :
			gzfile = SaveFile+".gz"
			files = open(gzfile, 'rb')
			upload = {'file': files}
			data = {'CustId':CustId, 'ScrapType':'cate' }
			Result_ = requests.post(NtosServer, data=data, files=upload)
			Result = Result_.text
			print(Result)
			if os.path.exists(gzfile) :
				os.remove(gzfile)
	time.sleep(random.randint(3, 6))     
print("end")
