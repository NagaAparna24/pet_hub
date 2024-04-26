from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path('viewpets',views.viewpets,name='viewpets'),
   path('rateus',views.rateus,name='rateus'),
   path('contactus',views.contactus,name='contactus'),
   path('viewproducts',views.viewproducts,name='viewproducts'),
   path('grooming_essentials',views.grooming_essentials,name='grooming_essentials'),
   path('enrichmentactivites',views.enrichmentactivites,name='enrichmentactivites'),
   path('donate',views.donate,name='donate'),
]
