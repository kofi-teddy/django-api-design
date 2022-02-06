import json 
from rest_framework import TestCase, Client
from rest_framework import status
from django.urls import reverse

from apps.puppies.models import Puppy
from apps.puppies.serializers import PuppySerializer


# initialize the APIClient app
client = Client()

class GetAllPuppiesTest(TestCase):
    '''
    Test module for GET all puppies API
    '''

    def setUp(self):
        Puppy.objects.create(name='Seph', age=24, breed='Bull Dog', color='Black')
        Puppy.objects.create(name='Yalanda', age=24, breed='Gradane', color='Brown')
        Puppy.objects.create(name='Eunice', age=24, breed='Labrador', color='Black')
        Puppy.objects.create(name='Serwaa', age=24, breed='Labrador', color='Brown')

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_puppies'))
        # get data from db
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)