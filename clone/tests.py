from django.test import TestCase
import datetime as dt
from .models import Profile,Image,Comment
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.Beryl= Profile(profile_photo = 'Cats',bio ='in the rari with no tint', user_id = 1)
    def test_instance(self):
        self.assertTrue(isinstance(self.Beryl,Profile))

    def test_save_method(self):
        self.Beryl.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        self.John.delete_profile
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)



