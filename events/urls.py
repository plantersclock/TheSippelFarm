from django.urls import path

from . import views
from . import forms

app_name = 'events'
urlpatterns = [
    path('home', views.HomeView.as_view(), name='user_home'),
    path('export', views.export_mixpanel, name='export_mixpanel'),
    path('brand_sql', views.create_brand_sql, name='create_brand_sql'),
    path('about_me', views.AboutView.as_view(), name='about_me'),
    ]
