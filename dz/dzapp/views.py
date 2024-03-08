from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Main page accessed')
    return HttpResponse("<h1>Привет!</h1><br><h4>Это мой сайт.</h4><br><a>...воот</a>")
def about(request):
    logger.info('About me page accessed')
    return HttpResponse("<h1>Привет!</h1><br><h4>Это страница про меня.</h4><br><a>здесь ничего нет0)</a>")

# Create your views here.
