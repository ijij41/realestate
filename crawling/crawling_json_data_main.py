#! /usr/bin/python
# -*- coding: utf-8 -*-


import access_web
import crawling_util
import address


deal_types=['1','2']   # houseType: 'DEAL','RENT'
deal_year=[x for x in range(2006, 2017, 1)]
deal_quarter=[x for x in range(1,5,1)]
deal_build=['A','B','C','E','F','G']   #menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND



deal_types=['1']   # houseType: 'DEAL','RENT'
deal_year=[2016]
deal_quarter=[4]
deal_build=['A']   #menuGubun:  APT,VILLA,HOUSE, OFFICETEL, RIGHT, LAND


def main():

    address_list = address.getAddressListFromDB()

    for build_type in deal_build:
        for deal_type in deal_types:
            for year in deal_year:
                for quarter in deal_quarter:
                    for address in address_list:

                        url  = crawling_util.buildUrl(build_type, deal_type, year,quarter,address['sido'], address['gugun'], address['dong'])
                        dict_return = access_web.access_web_retrun_dict(url)
                        deal_list = crawling_util.unrolling_deal_data(build_type, deal_type, year, quarter, address['sido'], address['gugun'],address['dong'],dict_return)






if __name__ == '__main__':
    main()




