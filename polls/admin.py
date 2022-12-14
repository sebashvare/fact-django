from django.contrib import admin

from .models import Question, Choice

"""
    Registro Admin Models: Question, Choice
"""
admin.site.register([Question, Choice])
