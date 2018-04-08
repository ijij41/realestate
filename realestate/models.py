# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# Create your models here.



class Address(models.Model):

    si_code = models.IntegerField()
    si_name = models.CharField(max_length=20)
    gu_code = models.IntegerField()
    gu_name = models.CharField(max_length=20)
    dong_code = models.BigIntegerField()
    dong_name = models.CharField(max_length=20)

    def __unicode__(self):
        # return self.dong_name
        return "%s %s %s %s %s %s" % (self.si_code, self.si_name, self.gu_code, self.gu_name, self.dong_code, self.dong_name)
        # return '%s' % str(self.si_code)


        # class Meta:
        #     managed = False
        #     db_table = 'address'


# class DealManager(models.Manager):
#     def
# @python_2_unicode_compatible
class Deal(models.Model):
    housetype = models.CharField(db_column='houseType', max_length=1)  # Field name made lowercase.
    dealtype = models.CharField(db_column='dealType', max_length=1)  # Field name made lowercase.

    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.

    # TODO can we do remove this field for removing duplicate
    sidocode = models.IntegerField(db_column='sidoCode')  # Field name made lowercase.
    guguncode = models.IntegerField(db_column='gugunCode')  # Field name made lowercase.
    dongcode = models.BigIntegerField(db_column='dongCode')  # Field name made lowercase.


    address = models.ForeignKey(Address, on_delete=models.CASCADE)


    deal_date = models.DateField(db_column='deal_data')

    bldg_cd = models.BigIntegerField(db_column='BLDG_CD', blank=True,
                                     null=True)  # Field name made lowercase.         //Building code
    bldg_area = models.FloatField(db_column='BLDG_AREA', blank=True, null=True)  # Field name made lowercase.
    bobn = models.CharField(db_column='BOBN', max_length=11, blank=True, null=True)  # Field name made lowercase.
    aptfno = models.CharField(db_column='APTFNO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deal_dd = models.CharField(db_column='DEAL_DD', max_length=11, blank=True, null=True)  # Field name made lowercase.
    deal_mm = models.IntegerField(db_column='DEAL_MM', blank=True, null=True)  # Field name made lowercase.
    bldg_nm = models.CharField(db_column='BLDG_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bubn = models.CharField(db_column='BUBN', max_length=100, blank=True, null=True)  # Field name made lowercase.

    build_year = models.IntegerField(db_column='BUILD_YEAR', blank=True, null=True)  # Field name made lowercase.
    sum_amt = models.IntegerField(db_column='SUM_AMT', blank=True, null=True)  # Field name made lowercase.
    rent_amt = models.IntegerField(db_column='RENT_AMT', blank=True, null=True)  # Field name made lowercase.
    tot_area = models.FloatField(db_column='TOT_AREA', blank=True, null=True)  # Field name made lowercase.
    bldg_muse_nm = models.CharField(db_column='BLDG_MUSE_NM', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    lawd_cd = models.BigIntegerField(db_column='LAWD_CD', blank=True, null=True)  # Field name made lowercase.
    umd_nm = models.CharField(db_column='UMD_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    right_gbn = models.IntegerField(db_column='RIGHT_GBN', blank=True, null=True)  # Field name made lowercase.


    # object  = DealManager()


    @property   #this is used at template, and view
    def get_housetype(self):
        housetypeDict = {'A': '아파트', 'B': '빌라/다세대', 'C': '단독/주택', 'E': '오피스텔', 'F': '분양권', 'G': '토지'}
        return housetypeDict[self.housetype]

    @property
    def get_dealtype(self):
        dealtypeDict = {'1': '매매','2':'임대'}   #refer to crawlling dealdate.py in crawling directory
        return dealtypeDict[self.dealtype]

    @property
    def get_address(self):
        return self.address.si_name + ", "+ self.address.gu_name + ", "+ self.address.dong_name + ", " + str(self.bobn) + " , " + str(self.bubn if not self.bubn==None else "")


    def get_all_field(self):
        return [f.name for f in self._meta.get_fields()]

    def __unicode__(self):
        field_values = []
        # http://freeprog.tistory.com/87
        # https: // stackoverflow.com / questions / 35926022 / django-str-return-all-the-attributes
        for field in self._meta.get_fields():
            field_data = getattr(self, field.name, '')

            if isinstance(field_data, unicode):
                field_data = field_data.encode('utf-8')
            else:
                field_data=str(field_data)

            # print field_data
            field_values.append(field_data)    # all values are no added 'u'.  In addition, I added
            # import sys
            # reload(sys)
            # sys.setdefaultencoding('utf-8')

        # print len(field_values), field_values
        # print ' ,'.join(field_values)
        return ' ,'.join(field_values)




    # def __unicode__(self):
    #     return self.bldg_nm
    # @classmethod
    # def dealtypeStr(cls, code):
    #     dealtypeDict = {'1': 'DEAL', '2': 'RENT'}
    #     return dealtypeDict[code]
    #
    # @classmethod
    # def housetypeStr(cls, code):
    #     housetypeDict = {'A': 'APT', 'B': 'VILLA', 'C': 'HOUSE', 'E': 'OFFICETEL', 'F': 'DEAL_RIGHT', 'G': 'LAND'}
    #     return housetypeDict[code]



    #
    # class Meta:
    #     managed = False
    #     db_table = 'deal'


