#! /usr/bin/python
# -*- coding: utf-8 -*-


import debug


#
# def getString(key, value):
#     if key=="build_type":
#
#         return
#     elif key=="deal_type":
#         print ""
#     else:
#         print "This is not valid type"
#
#         (crawling_util.get("build_type", build_type), crawling_util.get("deal_type", deal_type), year, quarter,
#          address['sido'] + address['gugun'] + address['dong'])

# def unrolling_deal_data(build_type, deal_type, year, quarter, sido, gugun, dong, json_data):
def unrolling_deal_data(json_data):
    # debug.debug_set(True)
    debug.debug_print(type(json_data))
    debug.debug_print(json_data)

    return_list = []

    for item in json_data["jsonList"]:

        # bobn = item["BOBN"]
        # assert item["AREA_ROW"]==1
        # assert item["AREA_CNT"]==1
        # bldg_area = item["BLDG_AREA"]
        # build_year = item["BUILD_YEAR"]
        # bldg_nm = item["BLDG_NM"]
        # bldg_cd = item["BLDG_CD"]

        for monthlist in [item["month1List"], item["month2List"], item["month3List"]]:
            for row in monthlist:
                # bobn = row["BOBN"]
                # build_year = row["BUILD_YEAR"]
                # bldg_area = row["BLDG_AREA"]
                # bldg_nm = row["BLDG_NM"]
                # sum_amt = row["SUM_AMT"]
                # deal_dd = row["DEAL_DD"]
                # bldg_cd = row["BLDG_CD"]
                # aptno=row["APTNO"]
                # deal_mm = row["DEAL_MM"]
                # bubn = row["BUBN"]

                # add new data
                return_list.append(row)

    for one_row in return_list:
        debug.debug_print(one_row)

    return return_list


def buildUrl(build_type, d_type, year, quarter, sidocode, guguncode, dongcode):
    url = "http://rt.molit.go.kr/srh/getListAjax.do?areaCode=&chosung=&danjiCode=&dongCode=" + dongcode + "&fromAmt1=&fromAmt2=&fromAmt3=&gubunCode=LAND&gugunCode=" + guguncode + "&houseType=" + d_type + "&jimokCode=&menuGubun=" + build_type + "&rentAmtType=3&reqPage=SRH&roadCode=&sidoCode=" + sidocode + "&srhPeriod=" + quarter + "&srhType=LOC&srhYear=" + year + "&toAmt1=&toAmt2=&toAmt3=&useCode=&useSubCode="
    return url

