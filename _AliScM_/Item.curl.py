# -*- coding: utf-8 -*- 
#알리 상품 모바일 curl

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

UserAgent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"	#_agent.get_mobile_agent()
headers = {
	"User-Agent":UserAgent
}
try : 
	cnt_ = int(1)
	for val in SiteUrlList :
		#저장html
		SaveHtml = ''
		#에러msg
		ErrMsg = ''
		
		PageHtml = ''
		PageHtmlJson = ''
		DetailUrl = ''
		DetailHtml = ''
		
		(SiteUrl, SaveFileName) = val.split("|@|")
		OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n\n"
		OriginUrl = OriginUrl + str(len(SiteUrlList))+" - "+str(cnt_)+"\n\n"
		
		#저장파일명
		SaveFile = FileDir+str(SaveFileName)
		SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
	  
		if SiteUrl == "" or SaveFileName == "" :
			print("continue - "+str(cnt_ ))
			continue
		print("ok - "+str(cnt_ ))
		cnt_ = cnt_ + 1
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
			ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"
		print(str(PageHtmlRecode))
		if PageHtml :
			try :
				PageHtml = re.sub('\n', '', PageHtml)
				PageHtmlJsonSearch = re.search(r'window.runParams\s+=\s+{\s+ data:(?P<JsonData>.*)};\s+</script>', str(PageHtml), re.DOTALL)
				PageHtmlJsonData = PageHtmlJsonSearch.group('JsonData')
				PageHtmlJson = json.loads(PageHtmlJsonData)
			except :
				PageHtmlJson = ''
				ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

		if PageHtmlJson :
			SaveHtml = SaveHtml + "<PageHtmlRecode>" + str(PageHtmlRecode) + "</PageHtmlRecode>\n\n"
			SaveHtml = SaveHtml + "<PageHtmlJson>" + str(PageHtmlJsonData) + "</PageHtmlJson>\n\n"
			try :
				DetailUrl = PageHtmlJson['descInfo']['productDescUrl']
			except :
				DetailUrl = '';
				ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

			if DetailUrl :
				try :
					if CookiesLang == "ko" :
						DetailHtml = requests.get(str(DetailUrl), headers=headers, cookies=cookies_ko)
					elif CookiesLang == "en" :
						DetailHtml = requests.get(str(DetailUrl), headers=headers, cookies=cookies_en)
					else :
						DetailHtml = requests.get(str(DetailUrl), headers=headers)
					DetailHtmlRecode = DetailHtml.status_code
					DetailHtml = DetailHtml.text
				except :
					DetailHtml = ''
					DetailHtmlRecode = 'error'
					ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

			if DetailHtml :
				DetailHtml = re.sub('(<script[^<]+</script>)', '', DetailHtml)
				DetailHtml = re.sub('(<a[^<]+</a>)', '', DetailHtml)
				DetailHtml = re.sub('(<link[^>]+>)', '', DetailHtml)
				SaveHtml = SaveHtml + "<DetailHtml>" + str(DetailHtml) + "</DetailHtml>\n\n"

		WriteFile = "<agent>"+str(UserAgent)+"</agent>"+"<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
		WriteFile = WriteFile + OriginUrl + SaveHtml + ErrMsg + "\n\n<PageHtml>"+str(PageHtml)+"</PageHtml>\n\n"

		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		os.system("gzip "+SaveFile)
		print(str(SaveFile))

		if FileSendSave == "Y" and NtosServer != "" :
			gzfile = SaveFile+".gz"
			files = open(gzfile, 'rb')
			upload = {'file': files}
			data = {'CustId':CustId, 'ScrapType':'item' }
			Result_ = requests.post(NtosServer, data=data, files=upload)
			Result = Result_.text
			if os.path.exists(gzfile) :
				os.remove(gzfile)
		time.sleep(random.randint(1, 3))
except :
	ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"
	print(ErrMsg)
