from django.urls import path
from . import views

"""
======================================================
Importamos todas las vistas definidas en nuestro APP, 
en este caso POLLS
======================================================
"""
app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/detalle", views.detail_questions, name="detalle_question"),
    path("<int:question_id>/votes", views.votes, name="votes"),
    path("results", views.results, name="results"),
    path("", views.index, name="index"),
]
