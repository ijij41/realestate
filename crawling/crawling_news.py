#!/usr/bin/env python3
#-*- coding: utf-8 -*

"""
"""


import django
from django.conf import global_settings
from mysite import settings as mysetting
django.conf.settings.configure(default_settings=global_settings, INSTALLED_APPS=mysetting.INSTALLED_APPS,
                               DATABASES=mysetting.DATABASES, DEBUG=True)
django.setup()



import datetime
from bs4 import BeautifulSoup

import time
import re
import requests
import sys

from re_news.models import News


def getNews(input_date):
    print input_date
    eval_d = input_date

    page_num = 1
    user_agent = "'Mozilla/5.0"
    headers ={"User-Agent" : user_agent}

    news_url_list = []

    # traverse all pages for one date
    while True:
        page_url = "http://news.naver.com/main/list.nhn?sid2=260&sid1=101&mid=shm&mode=LS2D&date=" + str(eval_d) + "&page=" + str(page_num) + ""
        # print page_url
        response = requests.get(page_url, headers=headers)
        html = response.text

        """
        주어진 HTML에서 기사 URL을 추출한다.
        """
        url_frags = re.findall('<a href="(.*?)"',html)
        urls = []
        for url_frag in url_frags:
            if "sid1=101&sid2=260" in url_frag and "aid" in url_frag:
                urls.append(url_frag)

        urls = list(set(urls))

        duplicate_url = False
        for url in urls:
            # print url
            if url in news_url_list:
                duplicate_url = True
                break
            news_url_list.append(url)

        if duplicate_url:
            break

        time.sleep(2)
        page_num += 1
        # break

    # get all news urls for all pages for one date
    # print len(news_url_list), news_url_list
    for news_url in news_url_list:
        # print new_url
        time.sleep(2)
        response = requests.get(news_url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')



        try:
            title =  soup.find(id = "articleTitle").get_text()
            date_time = soup.find("span","t11").get_text()
            content = soup.find(id = "articleBodyContents").get_text().split("function _flash_removeCallback() {}")[1].strip()
            news = News(title=title, news_pub_date=date_time, content=content, url=news_url)
            news.save()

        except AttributeError as e:
            print "AttributeError:", e
        except Exception as ex:
            print "Exception", ex





if __name__ == "__main__":
    # dt = datetime.datetime.now()
    dt = datetime.datetime(year=2018,month=4,day=1)
    dt = dt - datetime.timedelta(days=1)
    # dt1 = datetime.datetime(year=2018, month=4, day=18)
    # if dt == dt1:
    #     print "same"
    #     sys.exit(0)


    while(dt!=datetime.datetime(year=2017, month=1, day=1)):
        eval_d = dt.strftime("%Y%m%d")
        getNews(eval_d)
        dt = dt - datetime.timedelta(days=1)




