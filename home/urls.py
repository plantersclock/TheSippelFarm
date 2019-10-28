from django.urls import path

from . import views
from . import forms

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='user_home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    ]
