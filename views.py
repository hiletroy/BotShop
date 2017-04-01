import os
import requests
import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text

    webhook = reverse('telegrambot:webhook', kwargs={'token': '111111111111111111111111'})
    logger = logging.getLogger('my_app_name.my_new_module')
    logger.info(webhook)
    logger.info("!!!!!!!!!!!!!!")

    return HttpResponse('<pre>' + webhook + '</pre>')
