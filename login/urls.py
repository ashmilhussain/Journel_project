
from django.urls import path
from django.contrib import admin
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
  
	path('signup/', views.signup),
	path('login/', views.login),
]
