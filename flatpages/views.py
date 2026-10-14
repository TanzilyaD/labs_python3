from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'templates/index.html')


def hello(request):
    return HttpResponse(u'Привет, Мир!', content_type="text/plain; charset=utf-8")


def hello_default(request):
    return HttpResponse(u'Привет, Мир!')


def static_page(request):
    return render(request, 'templates/static_handler.html')