from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("registrarPersonaje/", views.registrarPersonaje),
    path("registrarUniverso/", views.registrarUniverso),
    path("crearUniverso/", views.crearUniverso),
    path("crearPersona/", views.crearPersona),
    path("modificarPersona/<codigo>", views.modificarPersona),
    path("modificarUniverso/<codigo>", views.modificarUniverso),
    path("editarPersona/", views.editarPersona),
    path("editarUniverso/", views.editarUniverso),
    path("eliminarPersona/<codigo>", views.eliminarPersona),
    path("eliminarUniverso/<codigo>", views.eliminarUniverso),
    path("infoUniverso/<codigo>", views.infoUniverso),
    path("infoPersonaje/<codigo>", views.infoPersonaje),
]