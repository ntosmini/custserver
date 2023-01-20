# -*- coding: utf-8 -*- 
# 테스트

import time
import sys
import json
import io
import os
import multiprocessing
import requests
import traceback
import random

SaveFile = "/home/ntosmini/public_html/_NtosSc_/test.html"
try :
  page_html = "test\n test"
  f = open(SaveFile, 'w', encoding="utf8")
  f.write(page_html)
  f.close()
  os.system("gzip "+SaveFile)
except :
  err = traceback.format_exc()
  print(str(err))
