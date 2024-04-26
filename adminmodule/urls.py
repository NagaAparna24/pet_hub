from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.projecthomepage,name='projecthomepage'),
    path('generalhomepage',views.generalhomepage,name='generalhomepage'),
    path('userhomepage', views.userhomepage, name='userhomepage'),
    path('Login',views.Login,name='Login'),
    path('Signup',views.Signup,name='Signup'),
    path('signup1',views.signup1,name='signup1'),
    path('login1',views.login1,name='login1'),
]
