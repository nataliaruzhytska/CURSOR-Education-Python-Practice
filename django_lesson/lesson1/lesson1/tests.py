from http import HTTPStatus

import requests
from django.test import TestCase
from django.urls import reverse

POCKEMON_URL = 'https://pokeapi.co/api/v2/'


class ViewTests(TestCase):

    def test_health_check(self):
        response = self.client.get(reverse('health_check'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pokemon_view(self):
        response = self.client.get(reverse('pokemon'))
        self.assertEqual(response.status_code, HTTPStatus.OK)


class DataTests(TestCase):

    def test_pokemon_data_returned(self):
        response = requests.get(f'{POCKEMON_URL}/type/3')
        data = response.json()['pokemon']
        name = [p['pokemon']['name'] for p in data]
        self.assertIsNotNone(response)
        self.assertIsNotNone(data, name)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pokemon_data_not_valid(self):
        data = [{}]
        data1 = 'data'
        data2 = None
        with self.assertRaises(KeyError):
            name = [p['name'] for p in data]
        with self.assertRaises(TypeError):
            name = [p['name'] for p in data1]
        with self.assertRaises(TypeError):
            name = [p['name'] for p in data2]
