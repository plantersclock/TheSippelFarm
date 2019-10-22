from django.urls import path

from . import views
from . import forms

app_name = 'events'
urlpatterns = [
    path('export', views.export_mixpanel, name='export_mixpanel'),
    path('brand_sql', views.create_brand_sql, name='create_brand_sql'),
    path('events', views.AboutView.as_view(), name='about_me'),
    path('', views.EventsView.as_view(), name='events'),
    ]
