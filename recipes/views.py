from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home 1')


def sobre(request):
    return HttpResponse(r'global-master\index.html')


def contato(request):
    return HttpResponse('contato 1')