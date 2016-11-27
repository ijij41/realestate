# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CustomChoiceField(forms.ChoiceField):
    #    def to_python(self, value):
    #       print "custom to_python"
    #       super(CustomChoiceField,self).to_python(value)

    # TODO: korean
    def validate(self, value):
        # print "xxx",SearchForm.end_year.value()
        # print "xxx", SearchForm.cleaned_data.get('description')
        # print "anananaan1", super(CustomChoiceField,self).widgets
        if value == "":
            raise ValidationError(
                # _('%(value)s is not an wow number'),
                _('You should select right area'),
                params={'value': value},
            )


# def validate_dong_code(value):
#    print "valide check: ", value
#    raise ValidationError(
#            _('%(value)s is not an wow number'),
#            params={'value': value},
#            )

#
# class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)




class SearchForm(forms.Form):
    # choices_data = ('1168010800','1111')
    # your_name = forms.CharField(label='Your name', max_length=100,validators=[validate_dong_code],required=False)
    # your_name = forms.CharField(label='Your name', max_length=100,validators=[validate_dong_code])
    # dong_code = forms.ChoiceField(widget=forms.Select, label = "", choices=(), required=False)
    # dong_code = forms.ChoiceField(widget=forms.Select, label = "", choices=(),)
    # dong_code = forms.ChoiceField(widget=forms.Select, label = "", choices=(), validators = [validate_dong_code])

    ##########################################################
    # deal_type : we don't need selet it due to default value

    CHOICES = [('1', '매매'), ('2', '전/월세')]

    YEARS = [(x, x) for x in range(2006, 2017)]
    QUARTERS = [(x, x) for x in range(1, 5)]

    deal_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial=1, )

    si_code = CustomChoiceField(label="", choices=())
    gu_code = CustomChoiceField(label="", choices=())
    dong_code = CustomChoiceField(label="", choices=())

    start_year = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class': 'form-control'}))
    start_quarter = forms.ChoiceField(choices=QUARTERS, widget=forms.Select(attrs={'class': 'form-control'}))
    end_year = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class': 'form-control'}))
    end_quarter = forms.ChoiceField(choices=QUARTERS, widget=forms.Select(attrs={'class': 'form-control'}))

    # priod : we don't need selet it due to default value

    def clean_end_quarter(self):
        data = self.cleaned_data['end_quarter']
        if False:
            raise ValidationError(
                # _('%(value)s is not an wow number'),
                _('XXX You should select right area'),
                params={'value': 3},
            )

        return data
