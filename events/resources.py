from tastypie.resources import ModelResource
from events.models import Event, EventJoined
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        filtering = {
            'name': ALL,
        }

class EventJoinedResource(ModelResource):
    event = fields.ForeignKey(EventResource, 'event', full=True)
    class Meta:
        queryset = EventJoined.objects.all()
        resource_name = 'eventjoined'
        filtering = {
            'rider': ALL,
            'event': ALL,
        }
