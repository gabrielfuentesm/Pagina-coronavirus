from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('hlascondes', views.Lascondes, name="hlascondes"), 
    path('contacto', views.contacto, name="contacto"),
    path('formulario2', views.formulario2, name="formulario2"),
    path('hvitacura', views.vitacura, name="hvitacura"),
    path('respuesta', views.respuesta, name="respuesta"),
    path('hbarnechea', views.lobarnechea, name="hbarnechea"),
]