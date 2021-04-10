from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.login, name='login'),
   path('home/', views.home, name='home'),
   path('data/', views.data, name='data'),
   path('status/', views.status, name='status'),

]
