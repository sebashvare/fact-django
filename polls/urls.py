from django.urls import path
from . import views

"""
======================================================
Importamos todas las vistas definidas en nuestro APP, 
en este caso POLLS
======================================================
"""

urlpatterns = [
    path("", views.index, name="index"),
    path("suma", views.nombre_usuario, name="index"),
]
