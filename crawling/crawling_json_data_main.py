#! /usr/bin/python
# -*- coding: utf-8 -*-

import crawling_address
import crawling_dealdata
import crawling_dealdata_to_file


def store_address_data_from_web():
    if not crawling_address.existData():
        crawling_address.run()
    else:
        print "there are already existing data"

    print "store crawling data db test"


def store_deal_data_from_web():
    crawling_dealdata.run()

def store_deal_data_to_file_from_web():
    crawling_dealdata_to_file.run()

    # if not crawling_dealdata.existData():
    #     crawling_dealdata.run()
    # else:
    #     print "there are already exist data"


def main():

    store_deal_data_from_web()
    # store_deal_data_to_file_from_web()


if __name__ == '__main__':


    main()
