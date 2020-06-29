from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('hlascondes', views.Lascondes, name="hlascondes"), 
    path('contacto', views.contacto, name="contacto")
]