import json 
from rest_framework import TestCase, Client
from django.urls import reverse

from apps.puppies.models import Puppy
from apps.puppies.serializers import PuppySerializer


# initialize the APIClient app
client = Client()

