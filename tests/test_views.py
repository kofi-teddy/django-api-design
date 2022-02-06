import json 
from django.test import TestCase, Client
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


class GetSinglePuppyTest(TestCase):
    '''
    Test module for GET single puppy API
    '''

    def setUp(self):
        self.ama = Puppy.objects.create(
            name='Steph', age=24, breed='Bull Dog', color='black' 
        )
        self.akos = Puppy.objects.create(
            name='Akos', age=24, breed='Gradane', color='brown' 
        )
        self.ricky = Puppy.objects.create(
            name='Ricky', age=24, breed='Labrador', color='black' 
        )
        self.rambo = Puppy.objects.create(
            name='Rambo', age=24, breed='Labrador', color='brown' 
        )

    def test_get_valid_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}),
        )
        puppy = Puppy.objects.get(pk=self.rambo.pk)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    
class CreateNewPuppyTest(TestCase):
    '''
    Test module for inserting a new puppy.
    '''

    def setUp(self):
        self.valid_payload = {
            'name': 'Ama',
            'age': 24,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'age': 24,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_puppy(self):
        response = client.post(
           reverse('get_post_puppies'),
           data=json.dumps(self.valid_payload),
           content_type='application/json' 
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)