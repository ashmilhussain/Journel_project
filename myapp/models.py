from django.db import models

# Create your models here.
#Login database 

class Login(models.Model):
#fields requireds.
	name=models.CharField(max_length= 20, help_text=" Enter your unique Id here")
	password=models.CharField(max_length=15, help_text=" Enter your password ")
	def __str__(self):
		return self.name