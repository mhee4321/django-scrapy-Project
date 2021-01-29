import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from stock.models import Stock

stock_code = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0] 
stock_code.sort_values(['상장일'], ascending=True)
stock_code = stock_code[['회사명', '종목코드']] 
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'}) 
stock_code.code = stock_code.code.map('{:06d}'.format) 

# company = input()
company = sys.argv[1]

code = stock_code[stock_code.company==company].code.values[0].strip()

url = 'http://finance.naver.com/item/sise.nhn?code={code}'.format(code=code)
print(url)

req_header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
res = requests.get(url, headers=req_header)
print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')

price = soup.select_one('div > p.no_today span.blind').get_text()
url = url

Stock(
    name=company,
    code=code,
    price=price,
    url = url
).save()

