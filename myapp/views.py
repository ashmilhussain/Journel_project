from django.shortcuts import render
from django.http import HttpRequest
from myapp.models import Login
# Create your views here.
def index(request):
	item=Login.objects.get(id=3)
	return render(request, 'index.html',{'item':item })