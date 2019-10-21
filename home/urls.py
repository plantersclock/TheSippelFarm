from django.urls import path

from . import views
from . import forms

app_name = 'home'
urlpatterns = [
    path('home', views.HomeView.as_view(), name='user_home'),
    path('export', views.export_mixpanel, name='export_mixpanel'),
    path('brand_sql', views.create_brand_sql, name='create_brand_sql'),
    path('', views.AboutView.as_view(), name='about_me'),
    ]
