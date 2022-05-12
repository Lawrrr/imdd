from datetime import date
from django.test import TestCase
from django.shortcuts import get_object_or_404

from ..models import Director

class DirectorTestCase(TestCase):
    def setUp(self):
        Director.objects.create(first_name='Johnny', last_name='Test', date_of_birth='1920-01-01')
        Director.objects.create(first_name='Bruce', last_name='Wayne', date_of_birth='1989-11-11')
        Director.objects.create(first_name='Guy', last_name='Gardner', date_of_birth='2000-06-21')

    def test_can_list_all_directors(self):
        directors = Director.objects.all()

        self.assertTrue(directors)

    def test_can_retrieve_director(self):
        director = Director.objects.get(id=1)

        self.assertEqual(director.id, 1)
        self.assertEqual(director.first_name, 'Johnny')
        self.assertEqual(director.last_name, 'Test')
        self.assertEqual(director.date_of_birth, date(1920, 1, 1))

    def test_can_create_director(self):
        director = Director.objects.create(first_name='Tootskie', last_name='Friend', date_of_birth='1940-02-02')

        self.assertEqual(director.first_name, 'Tootskie')
        self.assertEqual(director.last_name, 'Friend')
        self.assertEqual(director.date_of_birth, '1940-02-02')

    def test_can_update_director(self):
        directors = Director.objects.all()
        director = get_object_or_404(directors, pk=1)

        updateDirector = {
            'first_name': 'new',
            'last_name': 'name',
            'date_of_birth': '1999-04-21'
        }

        for key, value in updateDirector.items():
            setattr(director, key, value)

        director.save()

        self.assertEqual(director.first_name, 'new')
        self.assertEqual(director.last_name, 'name')
        self.assertEqual(director.date_of_birth, '1999-04-21')

    def test_can_delete_director(self):
        Director.objects.get(id=1).delete()
        deletedDirector = Director.objects.filter(id=1)

        self.assertFalse(deletedDirector)
