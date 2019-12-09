from django.urls import path
from django.conf.urls import url, include
from events.resources import EventResource, EventJoinedResource

from . import views
from . import forms

event_resource = EventResource()
event_joined_resource = EventJoinedResource()

app_name = 'events'
urlpatterns = [
    path('admin', views.EventAdminView.as_view(), name='event_admin'),
    path('live', views.LiveView.as_view(), name='live'),
    path('', views.EventsView.as_view(), name='events'),
    path('add', views.add_event, name='add_event'),
    path('edit/<int:pk>', views.edit_event, name="edit_event"),
    path('<int:pk>/sign_up', views.event_sign_up, name='sign_up'),
    path('<int:pk>/scheduler', views.attendee_schedule, name='scheduler'),
    url(r'ajax/attendee_defaults/$', views.attendee_defaults, name='attendee_defaults'),
    url(r'^api/', include(event_resource.urls)),
    url(r'^api/', include(event_joined_resource.urls)),
    ]
