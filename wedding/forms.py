

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

class Guest_Info(forms.Form):
    first_name= forms.CharField(max_length=100, required= False, widget = forms.TextInput(
        attrs={'required': 'True'}
    ))
    last_name= forms.CharField(max_length=100, required= False, widget= forms.TextInput(
        attrs={'required': 'True'}
    ))
    

