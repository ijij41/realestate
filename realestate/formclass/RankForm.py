# -*- coding: utf-8 -*-
import sys

from datetime import date

# from realestate.formclass.components.FormComponent import PirceScopeField
from realestate.formclass.components.FormComponent import MultiExampleField
from realestate.forms import CustomChoiceField
from realestate.models import Address

reload(sys)
sys.setdefaultencoding('utf-8')

from django import forms


class RankForm(forms.Form):
    # choices_data = ('1168010800','1111')
    # your_name = forms.CharField(label='Your name', max_length=100,validators=[validate_dong_code],required=False)
    # your_name = forms.CharField(label='Your name', max_length=100,validators=[validate_dong_code])
    # dong_code = forms.ChoiceField(widget=forms.Select, label = "", choices=(), required=False)
    # dong_code = forms.ChoiceField(widget=forms.Select, label = "", choices=(),)
    # dong_code = forms.ChoiceField(widget=forms.Select, label = "", choices=(), validators = [validate_dong_code])
    ##########################################################
    # deal_type : we don't need selet it due to default value

    DEAL_CHOICES = [('0','전체'), ('1', '매매'), ('2', '전/월세')]
    HOUSE_CHOICES = [('0','전체'), ('A','아파트'), ('B','빌라/다세대'), ('C', '단독/주택'), ('E', '오피스텔'), ('F','분양권'), ('G', '토지')]

    CUR_YEAR = date.today().year
    YEARS = [(x, x) for x in range(2006, CUR_YEAR+1)]
    QUARTERS = [(x, x) for x in range(1, 5)]

    rs_si_code_choice = Address.objects.all().values_list('si_code', 'si_name').distinct().order_by("si_name")
    rs_si_code_choice =  list(rs_si_code_choice)
    rs_si_code_choice.insert(0,(0,'시/도 선택'))
    # print type(rs_si_code_choice), rs_si_code_choice

    # print type(Address.objects.all().values_list('si_code', 'si_name', flat=True))
    # print 'zzz', type(rs_si_code_choice), rs_si_code_choice

    # rs_gu_code_choice = Address.objects.all().values_list('gu_code', 'gu_name').distinct()
    # rs_dong_code_choice = Address.objects.all().values_list('dong_code', 'dong_name').distinct()
    rs_gu_code_choice = [(0,'구/군 선택')]
    rs_dong_code_choice = [(0,'동 선택')]



    ################# form display ##########################
    start_year = forms.ChoiceField(label="년(시작)", choices=YEARS, widget=forms.Select(attrs={'class': 'form-control'}))
    start_quarter = forms.ChoiceField(label="분기(시작)", choices=QUARTERS,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    end_year = forms.ChoiceField(label="년(끝)", choices=YEARS, widget=forms.Select(attrs={'class': 'form-control'}))
    end_quarter = forms.ChoiceField(label="분기(끝)", choices=QUARTERS,
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    si_code = CustomChoiceField(label="시", choices=rs_si_code_choice,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    gu_code = CustomChoiceField(label="구", choices=rs_gu_code_choice,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    dong_code = CustomChoiceField(label="동", choices=rs_dong_code_choice,
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    house_type = forms.ChoiceField(label="주택유형", choices=HOUSE_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    deal_type = forms.ChoiceField(label="거래유형", choices=DEAL_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))


    deposit_price = MultiExampleField(label="보증금 가격")
    rent_price = MultiExampleField(label="월세 가격")

    users = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),label="라디오",)
    # cardio_training_days = forms.ChoiceField(widget=forms.CheckboxSelectMultiple,
    users.choices = [('0','a'), ('1', 'b'), ('2', 'c')]



    # deposit_price_start = forms.IntegerField(label="가격",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # deposit_price_start = forms.IntegerField(label="가격",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # deposit_price_end = forms.IntegerField(label="",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # deposit_price = DepositPriceField(label="가격",attrs={'class': 'form-control'})
    # rent_price  =



    ########################################################

    # address_keyword = forms.CharField(lable="주소 키워드")
    # keyword = forms.CharField(lable ="키워드")

    # priod : we don't need selet it due to default value

    # def clean_end_quarter(self):
    #     data = self.cleaned_data['end_quarter']
    #     if False:
    #         raise ValidationError(
    #             # _('%(value)s is not an wow number'),
    #             _('XXX You should select right area'),
    #             params={'value': 3},
    #         )
    #
    #     return data

