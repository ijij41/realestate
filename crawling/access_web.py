#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
import urllib2
import urlparse

import sys


def initial(url):
    # get
    # url = "http://rt.molit.go.kr/srh/getDanjiComboAjax.do?areaCode=&chosung=&danjiCode=&dongCode=1165010200&fromAmt1=&fromAmt2=&fromAmt3=&gubunCode=LAND&gugunCode=11650&houseType=1&menuGubun=A&rentAmtType=3&roadCode=&sidoCode=11&srhPeriod=4&srhType=LOC&srhYear=2016&toAmt1=&toAmt2=&toAmt3="

    # post (like get style url)
    # url = "http://rt.molit.go.kr/srh/getListAjax.do?areaCode=&chosung=&danjiCode=&dongCode=1165010200&fromAmt1=&fromAmt2=&fromAmt3=&gubunCode=LAND&gugunCode=11650&houseType=1&jimokCode=&menuGubun=A&rentAmtType=3&reqPage=SRH&roadCode=&sidoCode=11&srhPeriod=4&srhType=LOC&srhYear=2016&toAmt1=&toAmt2=&toAmt3=&useCode=&useSubCode="
    #############################################
    param_dict = dict(urlparse.parse_qsl(urlparse.urlsplit(url).query))
    pure_url = url.split("?")[0]
    #############################################

    # print param_dict
    # print pure_url

    req = urllib2.Request(pure_url)
    ################        POST data
    data = param_dict
    # opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    # the_page = opener.open(url, data=data).read()
    data = urllib.urlencode(data)
    req = urllib2.Request(pure_url, data)
    ###########################################

    ############### chanage header  ########################
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
    req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
    req.add_header("Accept-Language", "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3")
    req.add_header("Accept-Encoding", "gzip, deflate")
    req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    req.add_header("x-requested-with", "XMLHttpRequest")
    req.add_header("Referer", "http://rt.molit.go.kr/srh/srh.do?menuGubun=A&srhType=LOC&houseType=1&gubunCode=LAND")
    req.add_header("Connection", "keep-alive")
    ###########################################################

    return req


def access_web_retrun_json(url):
    req = initial(url)
    response = urllib2.urlopen(req)
    # headers = response.info().headers  # response header
    # the_page = response.read()
    js = json.loads(response.read())  # raw file is just str, so make it to dict, and then json dumps
    # print type(js),js
    jsonString = json.dumps(js, indent=4)
    # print type(jsonString),jsonString
    return jsonString


def access_web_retrun_dict(url):
    req = initial(url)

    success_access = False
    try:
        response = urllib2.urlopen(req)
        success_access = True
        # break
    except urllib2.URLError as ue:
        print ue

    if not success_access:
        print ("web access errors")
        return {'jsonList': None}

    # headers = response.info().headers  # response header
    # the_page = response.read()
    js_dict = json.loads(response.read())  # raw file is just str, so make it to dict, and then json dumps
    # print type(js),js
    # jsonString = json.dumps(js,indent=4)
    # print type(jsonString),jsonString
    return js_dict
