import sys
import os
import requests
import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from telegrambot.models import Bot, AuthToken
from telegram import Bot as BotAPI
from django.utils.html import escape



def index(request):
    # r = requests.get('http://httpbin.org/status/418')
    # print r.text

    # webhook = reverse('telegrambot:webhook', kwargs={'token': '339030622:AAGk24GWW40hJBfqOxqvhdsUJMw94zu5O98'})
    logger = logging.getLogger('my_app_name.my_new_module')
    #logger.info(webhook)

    # from django.contrib.sites.models import Site
    # current_site = Site.objects.get_current()
    # url = 'https://' + current_site.domain + webhook
    #url = 'https://tranquil-lake-76341.herokuapp.com/telegrambot/webhook/339030622:AAGk24GWW40hJBfqOxqvhdsUJMw94zu5O98'
    #url = 'https://tranquil-lake-76341.herokuapp.com/'
    #bot = BotAPI('339030622:AAGk24GWW40hJBfqOxqvhdsUJMw94zu5O98')
    # #bot.handle(Update.de_json(request.data, bot))
    #bot.setWebhook(webhook_url=url)
    logger.info(dir(request))
    print repr(request)
    sys.stdout.flush()
    return HttpResponse(escape(repr(request)))

    # return HttpResponse('<pre>' + webhook + '</pre>')
