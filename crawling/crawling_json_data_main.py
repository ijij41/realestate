#! /usr/bin/python
# -*- coding: utf-8 -*-


import access_web

def main():
    url = "http://rt.molit.go.kr/srh/getListAjax.do?areaCode=&chosung=&danjiCode=&dongCode=1165010200&fromAmt1=&fromAmt2=&fromAmt3=&gubunCode=LAND&gugunCode=11650&houseType=1&jimokCode=&menuGubun=A&rentAmtType=3&reqPage=SRH&roadCode=&sidoCode=11&srhPeriod=4&srhType=LOC&srhYear=2016&toAmt1=&toAmt2=&toAmt3=&useCode=&useSubCode="
    json_return = access_web.access_web_retrun_json(url)
    print json_return

if __name__ == '__main__':
    main()
