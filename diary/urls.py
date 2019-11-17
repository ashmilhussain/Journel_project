
from django.urls import path
from django.contrib import admin
from diary import views

urlpatterns = [
    path('admin/', admin.site.urls),
  
	path('diary/', views.diary),
]
