# import django
# from django.conf import global_settings
# from django.conf import settings
#
# from mysite import settings as mysetting
#
# django.conf.settings.configure(default_settings=global_settings, INSTALLED_APPS=mysetting.INSTALLED_APPS,
#                                DATABASES=mysetting.DATABASES, DEBUG=True)
# django.setup()
import sys

import datetime
import time

from django.db import OperationalError

import access_web
import crawling_util
from realestate.models import Deal, Address

deal_types_dict = {'1': 'DEAL', '2': 'RENT'}
deal_types = deal_types_dict.keys()  # houseType: 'DEAL','RENT'
deal_year = [x for x in range(2006, 2017, 1)]
deal_quarter = [x for x in range(1, 5, 1)]
deal_build_dict = {'A': 'APT', 'B': 'VILLA', 'C': 'HOUSE', 'E': 'OFFICETEL', 'F': 'DEAL_RIGHT', 'G': 'LAND'}
deal_build = deal_build_dict.keys()

deal_types = ['1','2']  # houseType: 'DEAL','RENT'
deal_year = [2016]
deal_quarter = [1,2]
# deal_build = ['A','B','C','E','F','G']  # menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND
deal_build = ['A','B','C','E','F','G']  # menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND


def run():
    address_list = Address.objects.all()

    for build_type in deal_build:
        for deal_type in deal_types:
            if (build_type is 'F' or build_type is 'G') and (deal_type is '2'):
                continue

            for year in deal_year:
                for quarter in deal_quarter:
                    for addr_idx, address in enumerate(address_list):
                        print addr_idx, address.dong_code, address.si_name, address.gu_name, address.dong_name, build_type, deal_type, year, quarter

                        # print "%s %s %s %s %s" % (
                        #     deal_build_dict[build_type], deal_types_dict[deal_type], year, quarter,
                        #     address.si_name + address.gu_name + address.dong_name)

                        url = crawling_util.buildUrl(build_type, deal_type, str(year), str(quarter),
                                                     str(address.si_code), str(address.gu_code), str(address.dong_code))

                        # dict_return = access_web.access_web_retrun_dict(url)
                        #
                        print url
                        success_access_web = False
                        for i in range(0, 5):
                            dict_return = access_web.access_web_retrun_dict(url)
                            if 'jsonList' in dict_return.keys() and (not dict_return['jsonList'] is None):
                                success_access_web = True
                                break

                            print "try count:", i, "   ", dict_return
                            time.sleep(60*10)


                        if not success_access_web:
                            print dict_return
                            sys.exit("Fail: web access")


                        print dict_return
                        # deal_list = crawling_util.unrolling_deal_data(build_type, deal_type, year, quarter, address['sido'],
                        #                                                   address['gugun'],
                        #                                                   address['dong'], dict_return)
                        deal_list = crawling_util.unrolling_deal_data(dict_return)

                        # print "unrolling deal list", deal_list
                        # if len(deal_list) > 4:
                        #     print "unrolling deal list", deal_list
                        #
                        #     # print type(deal_list[0])
                        #     # print Deal._meta.fields[15]
                        #     # print type(Deal._meta.fields[15])
                        #     # db_column_name_list = [x.db_column for x in Deal._meta.fields][9:]

                        bulk_list = []
                        for deal_item in deal_list:  # can be multiple rows
                            # per one row
                            d = Deal(housetype=build_type, dealtype=deal_type, year=year, period=quarter,
                                     sidocode=address.si_code, guguncode=address.gu_code,
                                     dongcode=address.dong_code)
                            d.deal_date = datetime.date(year, int(deal_item['DEAL_MM']),
                                                        int(deal_item['DEAL_DD'].split("~")[0]))
                            if 'BLDG_AREA' in deal_item.keys():
                                d.bldg_area = deal_item['BLDG_AREA']
                            if 'BOBN' in deal_item.keys():
                                d.bobn = deal_item['BOBN']
                            if 'APTFNO' in deal_item.keys():
                                d.aptfno = deal_item['APTFNO']
                            if 'DEAL_DD' in deal_item.keys():
                                d.deal_dd = deal_item['DEAL_DD']
                            if 'DEAL_MM' in deal_item.keys():
                                d.deal_mm = deal_item['DEAL_MM']
                            if 'BLDG_NM' in deal_item.keys():
                                d.bldg_nm = deal_item['BLDG_NM']
                            if 'BUBN' in deal_item.keys():
                                d.bubn = deal_item['BUBN']
                            if 'BLDG_CD' in deal_item.keys():
                                d.bldg_cd = deal_item['BLDG_CD']
                            if 'BUILD_YEAR' in deal_item.keys():
                                d.build_year = deal_item['BUILD_YEAR']
                            if 'SUM_AMT' in deal_item.keys():
                                d.sum_amt = int(deal_item['SUM_AMT'].replace(",", ''))
                            if 'RENT_AMT' in deal_item.keys():
                                d.rent_amt = int(deal_item['RENT_AMT'].replace(",", ''))
                            if 'TOT_AREA' in deal_item.keys():
                                d.tot_area = deal_item['TOT_AREA']
                            if 'BLDG_MUSE_NM' in deal_item.keys():
                                d.bldg_muse_nm = deal_item['BLDG_MUSE_NM']
                            if 'LAWD_CD' in deal_item.keys():
                                d.lawd_cd = deal_item['LAWD_CD']
                            if 'UMD_NM' in deal_item.keys():
                                d.umd_nm = deal_item['UMD_NM']
                            if 'RIGHT_GBN' in deal_item.keys():
                                d.right_gbn = deal_item['RIGHT_GBN']

                            bulk_list.append(d)
                            # save_success = False
                            # for try_idx in range(0, 3):
                            #     try:
                            #         d.save()
                            #         save_success = True
                            #         break
                            #     except OperationalError as oe:
                            #         print oe
                            #
                            # if not save_success:
                            #     sys.exit("db save error")

                        save_success = False
                        for try_idx in range(0, 3):
                            try:
                                Deal.objects.bulk_create(bulk_list)
                                save_success = True
                                break
                            except OperationalError as oe:
                                print oe
                                time.sleep(60*10)

                        if not save_success:
                            sys.exit("db save error")


def existData():
    return Deal.objects.all().count() > 0
