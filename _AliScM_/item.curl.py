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

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

IslId_SiteUrl = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

IslId_SiteUrl = MConfig['IslId_SiteUrl']
CustId = MConfig['CustId']

FileSendSave = MConfig['FileSendSave']  #저장후 전송여부
NtosServer = MConfig['NtosServer']  #전송서버 url

FileDir = MConfig['FileDir']  #저장폴더
UserAgent = MConfig['UserAgent']

for val in IslId_SiteUrl :
  #저장html
  SaveHtml = ''
  #에러msg
	ErrMsg = ''
	(SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n\n"
	#저장파일명
	SaveFile = FileDir+str(SaveFileName)
	SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
  
	if SiteUrl == "" or SaveFileName == "" :
		continue
  
	try :
		PageHtml = requests.get(SiteUrl)
		PageHtml = PageHtml.text
		PageHtmlRecode = PageHtml.status_code
	except :
		PageHtml = ''
		PageHtmlRecode = 'error'
		ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

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
		SaveHtml = SaveHtml + "<PageHtmlRecode>" + str(PageHtmlRecode) + "<PageHtmlRecode>\n\n"
		SaveHtml = SaveHtml + "<PageHtmlJson>" + str(PageHtmlJson) + "<PageHtmlJson>\n\n"
		try :
			DetailUrl = PageHtmlJson['descInfo']['productDescUrl']
		except :
			DetailUrl = '';
			ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

		if DetailUrl :
			try :
				DetailHtml = requests.get(str(DetailUrl))
				DetailHtml = DetailHtml.text
				DetailHtmlRecode = DetailHtml.status_code
			except :
				DetailHtml = ''
				DetailHtmlRecode = 'error'
				ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

		if DetailHtml :
			DetailHtml = re.sub('(<script[^<]+</script>)', '', DetailHtml)
			DetailHtml = re.sub('(<a[^<]+</a>)', '', DetailHtml)
			DetailHtml = re.sub('(<link[^>]+>)', '', DetailHtml)
			SaveHtml = SaveHtml + "<DetailHtml>" + str(DetailHtml) + "<DetailHtml>\n\n"

		WriteFile = "<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
		WriteFile = WriteFile + OriginUrl + SaveHtml + ErrMsg

		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		os.system("gzip "+SaveFile)

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
