
from django.urls import path
from django.contrib import admin
from django.conf.urls import url
#from . import views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
