from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def diary(request):
	return render(request, 'journel.html',{})

def login(request):
	return render(request, login.html,{})