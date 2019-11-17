from django.shortcuts import render
from django.http import HttpRequest
from myapp import birthday
from myapp.form import StuForm  
# Create your views here.

def profile(request):
	stu = StuForm()  
	return render(request, 'profiles.html', {'form':stu})


def index(request):
	profile
#	items=Login.objects.get(id=3)
	printDob=birthday.birthday('08/08/1994')
	return render(request, 'index.html', {'printDob':printDob}) # 'items':items})