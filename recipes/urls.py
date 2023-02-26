from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('astro/', views.berg),
    path('loja/', views.loja),
    path('recipes/<int:id>/', views.recipe)
    
]