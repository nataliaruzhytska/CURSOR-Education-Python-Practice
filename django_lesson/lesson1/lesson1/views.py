import requests

from django.http import HttpResponse
from django.shortcuts import render
from .settings import POCKEMON_URL


def health_check(request):
    return HttpResponse('OK')


def index(request):
    return HttpResponse(render(request, 'index.html'))


def pokemon(request):
    response = requests.get(f'{POCKEMON_URL}/type/3')
    data = [p['pokemon']['name'] for p in response.json()['pokemon']]
    return HttpResponse(render(request, 'pokemons.html', {'data': data}))
