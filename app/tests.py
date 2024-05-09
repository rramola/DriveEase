from django.test import TestCase
from app.models import *
# Create your tests here.
class TestListings(TestCase):
    def test_create_listing(self):
        profile = create_profile("Ryan", "Ryan@email.com")
        veh = create_vehicle(profile, 2006, "honda", "ridgeline")
        listing = create_listing(profile ,veh)
        print(listing.profile.email)