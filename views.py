import os
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text

    webhook = reverse('telegrambot:webhook', kwargs={'token': '111111111111111111111111'})

    return HttpResponse('<pre>' + webhook + '</pre>')
