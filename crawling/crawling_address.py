#! /usr/bin/python
# -*- coding: utf-8 -*-

import django
from django.conf import global_settings
from mysite import settings as mysetting

django.conf.settings.configure(default_settings=global_settings, INSTALLED_APPS=mysetting.INSTALLED_APPS,
                               DATABASES=mysetting.DATABASES, DEBUG=True)
django.setup()



import access_web
from realestate.models import Address


def existData():
    return Address.objects.count() > 0


def run():
    object_list = []
    sicode_list = {11: "서울특별시", 26: "부산광역시", 27: "대구광역시", 28: "인천광역시", 29: "광주광역시", 30: "대전광역시", 31: "울산광역시",
                   36: "세종특별자치시", 41: "경기도", 42: "강원도", 43: "충청북도", 44: "충청남도", 45: "전라북도", 46: "전라남도", 47: "경상북도",
                   48: "경상남도", 50: "제주특별자치도"}

    # sicode_list = {11: u"서울특별시", 26: u"부산광역시", 27: u"대구광역시", 28: u"인천광역시", 29: u"광주광역시", 30: u"대전광역시", 31: u"울산광역시",
    #                36: u"세종특별자치시", 41: u"경기도", 42: u"강원도", 43: u"충청북도", 44: u"충청남도", 45: u"전라북도", 46: u"전라남도", 47: u"경상북도",
    #                48: u"경상남도", 50: u"제주특별자치도"}

    for sicode in sicode_list.keys():
        print "start crawling : ", sicode_list[sicode]
        gugun_url = "http://rt.molit.go.kr/srh/getGugunListAjax.do?gubunCode=LAND&houseType=1&menuGubun=A&sidoCode=" + str(
            sicode) + "&srhPeriod=4&srhType=LOC&srhYear=2016"
        dict_gugun_return = access_web.access_web_retrun_dict(gugun_url)

        gugun_list = dict_gugun_return["jsonList"]
        for gugun_item in gugun_list:
            gugun_code = gugun_item["CODE"]
            gugun_name = gugun_item["NAME"]
            dong_url = "http://rt.molit.go.kr/srh/getDongListAjax.do?gubunCode=LAND&gugunCode=" + str(
                gugun_code) + "&houseType=1&menuGubun=A&sidoCode=" + str(
                sicode) + "&srhPeriod=4&srhType=LOC&srhYear=2016"
            dict_dong_return = access_web.access_web_retrun_dict(dong_url)

            dong_list = dict_dong_return["jsonList"]
            for dong_item in dong_list:
                dong_code = dong_item["CODE"]
                dong_name = dong_item["NAME"]
                addrObject = Address(si_code=sicode, si_name=sicode_list[sicode], gu_code=int(gugun_code),
                                     gu_name=gugun_name, dong_code=int(dong_code),
                                     dong_name=dong_name)

                # addrObject = Address(si_code=1, si_name='한글', gu_code=2, gu_name="넣어", dong_code=3,
                #                      dong_name="보자")
                object_list.append(addrObject)
                addrObject.save()

    print "Total address count :", len(object_list)

#
# start crawling :  충청북도
# start crawling :  세종특별자치시
# start crawling :  경기도
# start crawling :  강원도
# start crawling :  서울특별시
# start crawling :  충청남도
# start crawling :  전라북도
# start crawling :  전라남도
# start crawling :  경상북도
# start crawling :  경상남도
# start crawling :  제주특별자치도
# start crawling :  부산광역시
# start crawling :  대구광역시
# start crawling :  인천광역시
# start crawling :  광주광역시
# start crawling :  대전광역시
# start crawling :  울산광역시
# Total address count : 5039