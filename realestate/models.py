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


    def get_all_field_names(self):
        return [field.name if field.name != 'address' else 'address_id' for field in self._meta.get_fields()]

    def get_all_field_db_colums(self):
        return [field.db_column if field.name != 'address' else 'address_id' for field in self._meta.get_fields()]


    def get_all_field_types(self):
        return [type(field) if field.name != 'address' else type(field) for field in self._meta.get_fields()]

    def get_all_field_values(self):
        field_values = []
        # print "yy", self.get_all_field_names()

        for field_name in self.get_all_field_names():
            field_data = getattr(self, field_name, '')

            if isinstance(field_data, unicode):
                field_data = field_data.encode('utf-8')
            else:
                field_data = str(field_data)

            field_values.append(field_data)  # all values are no added 'u'.  In addition, I added

        return field_values






    @property
    def get_insertQuery(self):


        # field_names = self.get_all_field_names()
        field_columns = self.get_all_field_db_colums()
        field_types = self.get_all_field_types()
        field_values = self.get_all_field_values()

        column_str=''
        values_str = ''
        for c,t,v in zip(field_columns, field_types, field_values):
            # print c,t,v
            if t is models.fields.AutoField:
                continue

            column_str = column_str +'`'+ c + '`,'
            if t is models.fields.CharField or t is models.fields.DateField:
                if v == 'None':
                    values_str = values_str + "NULL,"
                else:
                    values_str = values_str + "'" + v + "',"
            elif t is models.fields.IntegerField:
                if v == 'None':
                    values_str = values_str + "NULL,"
                else:
                    values_str = values_str + str(int(v)) + ','
            else:
                if v == 'None':
                    values_str = values_str + "NULL,"
                else:
                    values_str = values_str + v + ','

        insert_q = "insert into "+str(self._meta.db_table)+"(%s) values(%s) " % (column_str[:-1], values_str[:-1])
        return insert_q




    def __unicode__(self):
        return ' ,'.join(self.get_all_field_values())




    #
    # class Meta:
    #     managed = False
    #     db_table = 'deal'


