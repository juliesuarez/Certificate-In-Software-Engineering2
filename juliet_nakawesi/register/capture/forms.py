from django.forms import ModelForm
from .models import *
from django import forms




class RegisterForm(ModelForm):
    district_choice = forms.ChoiceField(choices=[('district', 'District'),
                                                     ('state', 'State')], 
                                                     label='District or State')
    
    class Meta:
        model = Register
        fields = ['district_choice',  'district', 
                  'first_name', 'last_name','date_of_birth', 
                  'gender', 'district','town_zip_code', 
                  'country', 'phone_number1',
                  'phone_number2','email']


