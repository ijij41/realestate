from __future__ import unicode_literals

from django.db import models

# Create your models here.

#class Question_test(models.Model):
#    question_text_c = models.CharField(max_length=200)
#    #question_etc  = models.CharField(max_length=100)
#
#    def __unicode__(self):
#        return self.question_text_c
#
#
#
class Address(models.Model):

    si_code = models.IntegerField()
    si_name = models.CharField(max_length=20)
    gu_code = models.IntegerField()
    gu_name = models.CharField(max_length=20)
    dong_code = models.BigIntegerField()
    dong_name = models.CharField(max_length=20)

    def __unicode__(self):
	return self.dong_name

##    class Meta:
##        managed = False
##        db_table = 'address'
#
#

class Deal(models.Model):

    housetype = models.CharField(db_column='houseType', max_length=1)  # Field name made lowercase.
    dealtype = models.CharField(db_column='dealType', max_length=1)  # Field name made lowercase.

    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.

    sidocode = models.IntegerField(db_column='sidoCode')  # Field name made lowercase.
    guguncode = models.IntegerField(db_column='gugunCode')  # Field name made lowercase.
    dongcode = models.BigIntegerField(db_column='dongCode')  # Field name made lowercase.

    deal_date = models.DateField()

    bldg_area = models.FloatField(db_column='BLDG_AREA', blank=True, null=True)  # Field name made lowercase.
    bobn = models.CharField(db_column='BOBN', max_length=11, blank=True, null=True)  # Field name made lowercase.
    aptfno = models.CharField(db_column='APTFNO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deal_dd = models.CharField(db_column='DEAL_DD', max_length=11, blank=True, null=True)  # Field name made lowercase.
    deal_mm = models.IntegerField(db_column='DEAL_MM', blank=True, null=True)  # Field name made lowercase.
    bldg_nm = models.CharField(db_column='BLDG_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bubn = models.IntegerField(db_column='BUBN', blank=True, null=True)  # Field name made lowercase.
    bldg_cd = models.BigIntegerField(db_column='BLDG_CD', blank=True, null=True)  # Field name made lowercase.
    build_year = models.IntegerField(db_column='BUILD_YEAR', blank=True, null=True)  # Field name made lowercase.
    sum_amt = models.IntegerField(db_column='SUM_AMT', blank=True, null=True)  # Field name made lowercase.
    rent_amt = models.IntegerField(db_column='RENT_AMT', blank=True, null=True)  # Field name made lowercase.
    tot_area = models.FloatField(db_column='TOT_AREA', blank=True, null=True)  # Field name made lowercase.
    bldg_muse_nm = models.CharField(db_column='BLDG_MUSE_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lawd_cd = models.BigIntegerField(db_column='LAWD_CD', blank=True, null=True)  # Field name made lowercase.
    umd_nm = models.CharField(db_column='UMD_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    right_gbn = models.IntegerField(db_column='RIGHT_GBN', blank=True, null=True)  # Field name made lowercase.


    def __unicode__(self):
	return self.bldg_nm

#

#    class Meta:
#        managed = False
#        db_table = 'deal'
#