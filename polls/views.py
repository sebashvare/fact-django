from django.shortcuts import render, get_object_or_404
# Esta clase me permite ejecutar una respestuesta Http
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

"""
    Keyword arguments:
    Vistas basadas en funciones
    Return: return_description
"""

# Obtenemos todas las preguntas


def index(request):
    data_questions = Question.objects.all()
    return render(request, "polls/index.html", {"latest_question_list": data_questions})


"""
    Detail Questions:
    Obtenemos el detalle de las preguntas
    Return: 1 pregunta Segun su primary_Key
"""


def detail_questions(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"data": question})


def results(request):
    choice = Choice.objects.all()
    return render(request, "polls/results.html", {
        "data": choice
    })


def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        pregunta_seleccionada = question.choice_set.get(
            pk=request.POST["eleccion"])
        print("Respuesta", pregunta_seleccionada)
    except (KeyError, Choice.DoesNotExist):
        print("Estamos en el except")
        return render(request, "polls/detail.html", {
            "data": question,
            "mensaje_error": "No elegiste ninguna respuesta     "
        })
    else:
        pregunta_seleccionada.votes += 1
        pregunta_seleccionada.save()
        return HttpResponseRedirect(reverse('polls:results'))
