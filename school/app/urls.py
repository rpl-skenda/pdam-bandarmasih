from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.login),
   path('home/', views.home),
   path('data/', views.data),
   path('status/', views.status),

]
