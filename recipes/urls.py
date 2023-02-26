from django.urls import path
from recipes.views import home, berg, loja



urlpatterns = [
    path('', home),
    path('astro/', berg),
    path('loja/', loja)
    
]