from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def finance(request):
	return render(request, 'finance.html',{})