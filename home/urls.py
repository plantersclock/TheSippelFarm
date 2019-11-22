from django.urls import path

from . import views
from . import forms

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='user_home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('page/<str:name>/', views.page, name='page'),
    path('contact-us/<str:ref>/', views.contact_us, name='contact_us'),
    ]
