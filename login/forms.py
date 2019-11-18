from django import forms
from .models import Siteuser

GENDER_CHOICES= [
    ('First choice', 'I am...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]

COUNTRY_CHOICES= [
    ('France', 'France'),
    ('Germany', 'Germany'),
    ('Italy', 'Italy'),
    ('United States', 'United States'),
    ]

YEARS= [x for x in range(1920,2017)]


class Signupform(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    birth_date= forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    gender= forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    location= forms.CharField(widget=forms.Select(choices=COUNTRY_CHOICES))
    

    class Meta:
        model= Siteuser
        fields= ["firstname", "lastname",
                 "username", "password1",
                 "password2",
                 "birth_date",
                 "gender",
                 "email", "phone", 
                 "location"]
