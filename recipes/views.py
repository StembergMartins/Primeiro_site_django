from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'recipes/pages/home.html', context={
        'name' : 'Stemberg Carvalho'
    })

def berg(request):
    return render(request, 'recipes/astro/index.html')

def loja(request):
    return render(request, 'recipes/loja/index.html')

def recipe(request, id):
    return render(request,'recipes/pages/home.html', context={
        'name' : 'Stemberg Carvalho'
    })