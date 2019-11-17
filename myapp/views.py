from django.shortcuts import render
from django.http import HttpRequest
from myapp import birthday
from myapp.models import Login

# Create your views here.

def profile(request):
	personal={'address':'Electronic city, Bangalore',}
	return render(request, 'profile.html', {'personal':personal})

def index(request):
	profile
	items=Login.objects.get(id=3)
	printDob=birthday.birthday('08/08/1994')
	return render(request, 'index.html', {'printDob':printDob,'items':items})