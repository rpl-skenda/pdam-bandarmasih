from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.loginPage, name='login'),
   path('logout/', views.logoutUser, name='logout'),

   path('', views.home, name='home'),
   path('data/', views.data, name='data'),
   path('dataTukang/', views.dataTukang, name='dataTukang'),

   path('status/', views.status, name='status'),
   path('create/', views.create, name='create'),

   path('update/<str:pk>/', views.update, name="update"),
   path('delete/<str:pk>/', views.delete, name="delete"),
   path('updatestatus/<str:pk>/', views.update_status, name="updateStatus"),
]