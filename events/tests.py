from datetime import datetime, timedelta

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from travel.models import Trip, TripUser
from django.contrib.auth.models import User


class TestPermissions(TestCase):
    def test_owner_can_view_trips(self):
        owner = User.objects.create_user("cutie", password="secret")
        owner.save()

        trip = Trip(name="My Trip", budget=100, travelers=1, start_date=datetime.now(timezone.utc), end_date=datetime.now(timezone.utc) + timedelta(days=1), notes="meow")
        trip.save()
        trip_user = TripUser(trip=trip, user=owner, role="")
        trip_user.save()

        self.client.login(username="cutie", password="secret")
        response = self.client.get(reverse("travel:my_trip", args=[trip.id]))
        self.assertEquals(200, response.status_code)


    def test_rando_cannot_view_trip(self):
        owner = User.objects.create_user("cutie", password="secret")
        owner.save()

        trip = Trip(name="My Trip", budget=100, travelers=1, start_date=datetime.now(timezone.utc), end_date=datetime.now(timezone.utc) + timedelta(days=1), notes="meow")
        trip.save()
        trip_user = TripUser(trip=trip, user=owner, role="")
        trip_user.save()

        rando = User.objects.create_user("rando", password="notsecret")
        rando.save()

        self.client.login(username="rando", password="notsecret")
        response = self.client.get(reverse("travel:my_trip", args=[trip.id]))
        self.assertEquals(404, response.status_code)
