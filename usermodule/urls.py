from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path('returnandrequest',views.returnandrequest,name='returnandrequest'),
   path('Logout', views.Logout, name='Logout'),
   path('petmanagement',views.petmanagement,name='petmanagement'),
   path('articles',views.articles,name='articles'),
   path('success_page', views.success_page, name='success_page'),

]
