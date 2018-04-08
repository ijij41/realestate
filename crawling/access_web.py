#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
import urllib2
import urlparse

import sys


def make_post_req(url):
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
    print "pure_url: ", pure_url
    print "param_dict: ", data
    data = urllib.urlencode(data)
    #print "param_dict: ",json.dumps(data)
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

    ###########################################################
#    req.add_header("Accept","application/json, text/javascript, */*; q=0.01")
#    req.add_header("Accept-Encoding","gzip, deflate")
#    req.add_header("Accept-Language","ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")
#    req.add_header("Connection","keep-alive")
#    #req.add_header("Content-Length","291")
#    req.add_header("Content-Type","application/x-www-form-urlencoded; charset=UTF-8")
#    req.add_header("Cookie","ROUTEID=.HTTP1; JSESSIONID=FE33C47C8999F08838041933DBB7C288")
#    req.add_header("Host","rt.molit.go.kr")
#    req.add_header("Origin","http://rt.molit.go.kr")
#    req.add_header("Referer","http://rt.molit.go.kr/srh/srh.do?menuGubun=A&srhType=LOC&houseType=1&gubunCode=LAND")
#    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
#    req.add_header("X-Requested-With","XMLHttpRequest")
    ###########################################################

    return req



def access_web_retrun_json(url):
    req = make_post_req(url)
    response = urllib2.urlopen(req)
    # headers = response.info().headers  # response header
    # the_page = response.read()
    js = json.loads(response.read())  # raw file is just str, so make it to dict, and then json dumps
    # print type(js),js
    jsonString = json.dumps(js, indent=4)
    # print type(jsonString),jsonString
    return jsonString


def access_web_retrun_dict(url):
    req = make_post_req(url)

    success_access = False
    try:
        response = urllib2.urlopen(req)
        success_access = True
	print "web access success"
        # break
    except urllib2.URLError as ue:
        print 'error url:', url
        print ue
    except Exception as ex:
	print ex;
	

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
