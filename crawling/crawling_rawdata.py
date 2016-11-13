#! /usr/bin/python
# -*- coding: utf-8 -*-


import urllib
import urllib2
import urlparse 


#reference
#basic: http://j4ckp4rd.tistory.com/17
#debug: http://stackoverflow.com/questions/6348499/making-a-post-call-instead-of-get-using-urllib2


# get
#url = "http://rt.molit.go.kr/srh/getDanjiComboAjax.do?areaCode=&chosung=&danjiCode=&dongCode=1165010200&fromAmt1=&fromAmt2=&fromAmt3=&gubunCode=LAND&gugunCode=11650&houseType=1&menuGubun=A&rentAmtType=3&roadCode=&sidoCode=11&srhPeriod=4&srhType=LOC&srhYear=2016&toAmt1=&toAmt2=&toAmt3="

# post 
url = "http://rt.molit.go.kr/srh/getListAjax.do?areaCode=&chosung=&danjiCode=&dongCode=1165010200&fromAmt1=&fromAmt2=&fromAmt3=&gubunCode=LAND&gugunCode=11650&houseType=1&jimokCode=&menuGubun=A&rentAmtType=3&reqPage=SRH&roadCode=&sidoCode=11&srhPeriod=4&srhType=LOC&srhYear=2016&toAmt1=&toAmt2=&toAmt3=&useCode=&useSubCode="


#############################################
param_dict = dict(urlparse.parse_qsl(urlparse.urlsplit(url).query))
url  = urlparse.urlsplit(url).geturl()
url = "http://rt.molit.go.kr/srh/getListAjax.do"
#############################################

print param_dict
print url

req = urllib2.Request(url)

################        POST data 
data = param_dict 
#opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
#the_page = opener.open(url, data=data).read()
data = urllib.urlencode(data)
req = urllib2.Request(url, data)
###########################################

############### chanage header  ########################
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
req.add_header("Accept-Language", "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3")
req.add_header("Accept-Encoding","gzip, deflate")
req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
req.add_header("x-requested-with","XMLHttpRequest")
req.add_header("Referer","http://rt.molit.go.kr/srh/srh.do?menuGubun=A&srhType=LOC&houseType=1&gubunCode=LAND")
req.add_header("Connection","keep-alive")
###########################################################

response = urllib2.urlopen(req)
headers = response.info().headers #response header
the_page = response.read()
 
print the_page
