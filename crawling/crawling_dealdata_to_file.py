
import django
from django.conf import global_settings
from mysite import settings as mysetting

django.conf.settings.configure(default_settings=global_settings, INSTALLED_APPS=mysetting.INSTALLED_APPS,
                               DATABASES=mysetting.DATABASES, DEBUG=True)
django.setup()


import sys

import datetime
import time

from django.db import OperationalError

import access_web
import crawling_util
from realestate.models import Deal, Address

from django.db import connection





deal_types_dict = {'1': 'DEAL', '2': 'RENT'}
deal_types = deal_types_dict.keys()  # houseType: 'DEAL','RENT'
deal_year = [x for x in range(2006, 2017, 1)]
# deal_year = [x for x in range(2016, 2017, 1)]
deal_quarter = [x for x in range(1, 5, 1)]
deal_build_dict = {'A': 'APT', 'B': 'VILLA', 'C': 'HOUSE', 'E': 'OFFICETEL', 'F': 'DEAL_RIGHT', 'G': 'LAND'}
deal_build = deal_build_dict.keys()



deal_year = [2006]
#deal_quarter = [1, 2, 3, 4]
#deal_quarter = [1,2]
#deal_quarter = [3,4]
# # deal_build = ['A','B','C','E','F','G']  # menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND
deal_build = ['A', 'B', 'C', 'E', 'F', 'G']  # menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND
#deal_build = ['E', 'F', 'G']  # menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND
#deal_build = ['E']  # menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND
deal_types = ['1', '2']  # houseType: 'DEAL','RENT'

#intermittent_sleep_time = 60*3
# intermittent_sleep_time = 60*1
intermittent_sleep_time = 40
#web_access_retry_time = 60*10
#db_save_retry_time = 60*10
web_access_retry_time = 60*10
db_save_retry_time = 60*10






def run():
    # NOTE: this codes should be executed based on address

    address_list = Address.objects.all()
    compare_insert_row = 1

    t1 = time.time()


    for year in deal_year:
        for quarter in deal_quarter:
            f = open('db_query_collection_'+str(year)+'_'+str(quarter)+'.sql', 'w')
            for build_type in deal_build:
                for deal_type in deal_types:
                    total_insert_row = 0
                    if (build_type is 'F' or build_type is 'G') and (deal_type is '2'):
                        continue

                    # continue

                    for addr_idx, address in enumerate(address_list):
                        # if (addr_idx + 1) % 50 == 0:
                        # if (addr_idx + 1) % 2 == 0:
                        time.sleep(intermittent_sleep_time)

                        # print addr_idx, address.dong_code, address.si_name, address.gu_name, address.dong_name, build_type, deal_type, year, quarter

                        # print "%s %s %s %s %s" % (
                        #     deal_build_dict[build_type], deal_types_dict[deal_type], year, quarter,
                        #     address.si_name + address.gu_name + address.dong_name)

                        url = crawling_util.buildUrl(build_type, deal_type, str(year), str(quarter),
                                                     str(address.si_code), str(address.gu_code), str(address.dong_code))



                        # s = "reqPage = SRH&menuGubun = A & srhType = LOC & houseType = 1 & srhYear = 2018 & srhPeriod = 1 & gubunCode = LAND & sidoCode = 11 & gugunCode = 11680 & dongCode = 1168010300 & chosung = & roadCode = & danjiCode = & rentAmtType = 3 & fromAmt1 = & toAmt1 = & fromAmt2 = & toAmt2 = & fromAmt3 = & toAmt3 = & areaCode = & jimokCode = & useCode = & useSubCode = & jibun = & typeGbn ="
                        # url = "".join(s.split())
                        # url = "http://rt.molit.go.kr/srh/getListAjax.do?"+url


                        print "url:", url
                        success_access_web = False
                        for i in range(0, 10):
                            try:
                                dict_return = access_web.access_web_retrun_dict(url)
                                if 'jsonList' in dict_return.keys() and (not dict_return['jsonList'] is None):
                                    success_access_web = True
                                    break

                            except OperationalError as oe:
                                print oe
                            except Exception as e:
                                print e

                            print "re-try count due to some exception:", i, "   ", dict_return
                            t2 = time.time()
                            print t2 - t1
                            time.sleep(web_access_retry_time)   #end of for

                        if not success_access_web:
                            print dict_return
                            t2 = time.time()
                            print t2 - t1
                            sys.exit("Fail: web access")

                        # print dict_return
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
                        print "deal_list for db save:", len(deal_list), deal_list
                        #bulk_list = []
                        for deal_item in deal_list:  # can be multiple rows
                            # per one row
                            d = Deal(housetype=build_type, dealtype=deal_type, year=year, period=quarter,
                                     sidocode=address.si_code, guguncode=address.gu_code,
                                     dongcode=address.dong_code)

                            # d = Deal(housetype=deal_item['houseType'], dealtype=deal_item['dealType'], year=deal_item['Year'], period=deal_item['Period'],
                            #          sidocode=deal_item['sidoCode'], guguncode=deal_item['gugunCode'],
                            #          dongcode=deal_item['dongCode'])

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

                            d.address_id = address.pk

                            #bulk_list.append(d)
                            # print "Save Data:", d
                            print "Save Data Query:", d.get_insertQuery
                            f.write(d.get_insertQuery+"\n")
                            f.flush()


                            # save_success = False
                            # for try_idx in range(0, 3):
                            #     try:
                            #         # d.save()
                            #         print "raw query:", connection.queries[-1]
                            #         save_success = True
                            #         break
                            #     except OperationalError as oe:
                            #          print "Custom error", oe
                            #
                            #     time.sleep(db_save_retry_time)
                            #
                            # if not save_success:
                            #     sys.exit("db save error!!")

                        # sys.exit(0)




                    print "Year:", year, "Quarter:", quarter, "BuildType:", build_type, "DealType:", deal_type, "Total DB insert count:", total_insert_row

            f.close()

    t2 = time.time()
    print t2 - t1



if __name__ == "__main__":
    run()


