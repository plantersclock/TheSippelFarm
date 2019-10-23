from django.urls import path

from . import views
from . import forms

app_name = 'events'
urlpatterns = [
    path('events', views.AboutView.as_view(), name='about_me'),
    path('', views.EventsView.as_view(), name='events'),
    path('<int:pk>/sign_up', views.event_sign_up, name='sign_up'),
    path('<int:pk>/scheduler', views.attendee_schedule, name='scheduler'),
    ]
