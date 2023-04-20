from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache


# Create your views here.
def set(request):
    cache.set('message', '奥利给！', 120)
    return HttpResponse('已经储存缓存')

def get(request):
    return HttpResponse(cache.get('message'))
