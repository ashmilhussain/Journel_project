from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from diary import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('diary/', include('diary.urls')),
#    url('login/', views.login),
    path('login/', include('login.urls')),
]

"""
from django.contrib import admin
from django.urls import path
#import django.conf.urls
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('index/', views.index),
]
"""