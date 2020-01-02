import requests

from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from .settings import POCKEMON_URL


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

    def test_pokemon_api_response(self):
        response = requests.get(f'{POCKEMON_URL}/type/3')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pokemon_data_returned(self):
        response = requests.get(f'{POCKEMON_URL}/type/3')
        data = response.json()['pokemon']
        name = [p['pokemon']['name'] for p in data]
        self.assertIsNotNone(data, name)

    def test_pokemon_data_not_valid(self):
        data = [{}]
        with self.assertRaises(KeyError):
            name = [p['name'] for p in data]

    def test_pokemon_data_not_valid_1(self):
        data1 = 'data'
        with self.assertRaises(TypeError):
            name = [p['name'] for p in data1]

    def test_pokemon_data_not_valid_2(self):
        data2 = None
        with self.assertRaises(TypeError):
            name = [p['name'] for p in data2]