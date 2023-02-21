from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'recipes/home.html', context={
        'name' : 'Stemberg Carvalho'
    })


def sobre(request):
    return render(request, 'global/home.html')


def contato(request):
    return render(request,'recipes/contato.html')


def contato(request):
    return render(request,'recipes/index.html')