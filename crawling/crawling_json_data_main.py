#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
settings.configure(DEBUG=True)


import access_web
import address
import crawling_util
from realestate.models import Address

deal_types=['1','2']   # houseType: 'DEAL','RENT'
deal_year=[x for x in range(2006, 2017, 1)]
deal_quarter=[x for x in range(1,5,1)]
deal_build=['A','B','C','E','F','G']   #menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND


deal_types=['1']   # houseType: 'DEAL','RENT'
deal_year=[2016]
deal_quarter=[4]
deal_build=['A']   #menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND






def store_address_data_from_web():
    addr = Address(si_code=1, si_name='test_crawling', gu_code=2, gu_name="gu_test", dong_code=3, dong_name="dong_test")
    # addr.save()
    print "store crawling data db test"





def store_deal_data_from_web():

    # address_list = address.getAddressListFromDB()

    for build_type in deal_build:
        for deal_type in deal_types:
            for year in deal_year:
                for quarter in deal_quarter:
                    # for address in address_list:

                        url  = crawling_util.buildUrl(build_type, deal_type, year, quarter, address['sido'], address['gugun'], address['dong'])
                        dict_return = access_web.access_web_retrun_dict(url)
                        deal_list = crawling_util.unrolling_deal_data(build_type, deal_type, year, quarter, address['sido'], address['gugun'],
                                                                      address['dong'], dict_return)



def main():

    store_address_data_from_web()
    # store_deal_data_from_web()









if __name__ == '__main__':
    main()




