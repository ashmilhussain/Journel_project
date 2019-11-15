from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def login(request):
	return render(request, 'login.html',{})