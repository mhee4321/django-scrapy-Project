import requests
import json
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from news.models import News


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__=='__main__':
    
    # News.objects.all().delete()

    uri = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'

    req_header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    res = requests.get(uri, headers=req_header)
    print(res.status_code)

    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline dl dt:nth-child(2) a')

    contents = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline dl dd span.lede')

    companies = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline dl dd span.writing')

    saved_times = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline dl dd span.date.is_new')

    ts = []
    cs = []
    ps = []
    ds = []
    for i in titles:
        ts.append(i.text)

    for i in contents:
        cs.append(i.text)

    for i in companies:
        ps.append(i.text)

    for i in saved_times:
        ds.append(i.text)

    for item in zip(ts,cs,ps,ds):
        News(
            title=item[0],
            content=item[1],
            company=item[2],
            saved_time=item[3]
        ).save()




