import pickle

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from django import forms

# class PhoneNumberField(forms.ChoiceField):
#     pass

#
from django.forms import CharField, MultiWidget


# class PirceScopeField(forms.MultiValueField):
#     def __init__(self, **kwargs):
#         # Define one message for all fields.
#         error_messages = {
#             'incomplete': 'Enter a country calling code and a phone number.',
#         }
#         # Or define a different message for each field.
#         fields = (
#             CharField(
#                 error_messages={'incomplete': 'Enter a country calling code.'},
#                 validators=[
#                     RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
#                 ],
#             ),
#             CharField(
#                 error_messages={'incomplete': 'Enter a phone number.'},
#                 validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
#             ),
#             CharField(
#                 validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
#                 required=False,
#             ),
#         )
#         super(PirceScopeField, self).__init__(
#             error_messages=error_messages, fields=fields,
#             require_all_fields=False, **kwargs
#         )


class MultiWidgetBasic(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = [forms.TextInput(),
                   forms.TextInput()]
        super(MultiWidgetBasic, self).__init__(widgets, attrs)

    def render(self, name, value, attrs=None):
        output = MultiWidget.render(self, name, value)
        output = output.replace("/><i","/>~<i")
        print output
        return output

    # #     MultiWidget.render(self,name,value)
    # def render(self, *args, **kwargs):
    #     output = super(CheckboxSelectMultipleP, self).render(*args, **kwargs)
    #     return mark_safe(output.replace(u'<ul>', u'').replace(u'</ul>', u'').

    def decompress(self, value):
        if value:
            return pickle.loads(value)
        else:
            return ['', '']


class MultiExampleField(forms.MultiValueField):
    widget = MultiWidgetBasic(attrs={'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        list_fields = [forms.CharField(max_length=10),
                       forms.CharField(max_length=10)]
        super(MultiExampleField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        ## compress list to single object
        ## eg. date() >> u'31/12/2012'
        return pickle.dumps(values)

