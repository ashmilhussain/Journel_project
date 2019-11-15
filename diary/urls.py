
from django.urls import path
from django.contrib import admin
from diary import views
from myapp import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
	path('diary/', v.index),
]
