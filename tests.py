from django.test import TestCase
from apps.puppies.models import Puppy


class PuppyTest(TestCase):
    '''
    Test module for Puppy model
    '''

    def setUp(self):
        Puppy.objects.create(name='Ama', age=24, breed='Bull Dog', color='Black')
        Puppy.objects.create(name='Akos', age=24, breed='Gradane', color='Brown')

    def test_puppy_breed(self):
        puppy_ama = Puppy.objects.get(name='Ama')
        puppy_akos = Puppy.objects.get(name='Akos')
        self.assertEqual(puppy_ama.get_breed(), 'Ama belongs to Bull Dog breed.')
        self.assertEqual(puppy_akos.get_breed(), 'Akos belongs to Gradane breed.')