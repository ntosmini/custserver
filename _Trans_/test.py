# -*- coding: utf-8 -*- 
#구글번역 

import time
import sys
import json
import io
import os
import requests
import googletrans
import traceback

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

translator = googletrans.Translator()
TransStr = "hello"
ResultStr = translator.translate(str(TransStr), dest = 'ko', src = 'en')

print(str(TransStr)+" >> "+ResultStr.text)
