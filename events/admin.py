from django.contrib import admin
from .models import  Event, Professional, EventJoined

# Register your models here.

admin.site.register(Event)
admin.site.register(Professional)
admin.site.register(EventJoined)

