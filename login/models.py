from django.db import models
from .validators import(validate_firstname_length,
 validate_lastname_length,
 validate_username_length, validate_username_alphadigits,
 validate_password_length, validate_password_digit,
 validate_password_uppercase, 
 validate_phonenumber)



class Siteuser(models.Model):
    firstname= models.CharField(max_length=100, verbose_name='First name', validators= [validate_firstname_length])
    lastname= models.CharField(max_length=100, verbose_name='Last name', validators= [validate_lastname_length])
    username= models.CharField(max_length=25, verbose_name= 'User name', validators= [validate_username_length, validate_username_alphadigits])
    password1= models.CharField(max_length=30, validators=[validate_password_length, validate_password_digit, validate_password_uppercase])
    password2= models.CharField(max_length=30)
    birth_date= models.DateField(verbose_name='What is your birth date?')
    gender= models.CharField(max_length=6)
    email= models.EmailField()
    phone= models.CharField(max_length= 15, validators= [validate_phonenumber])
    location= models.CharField(max_length=100)
