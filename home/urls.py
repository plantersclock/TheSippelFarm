from django.urls import path

from . import views
from . import forms

app_name = 'home'
urlpatterns = [
    path('home', views.HomeView.as_view(), name='user_home'),
    path('', views.AboutView.as_view(), name='about_me'),
    ]
