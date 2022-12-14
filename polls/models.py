from django.db import models

"""
================================================
        Creacion Modelos de la APP 
        Questions, Choices
================================================
"""

"""
    Documentacion Django QuerySet: https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups
"""


class Question(models.Model):

    question_text = models.CharField(
        max_length=200,
        help_text="Ingresa la pregunta")

    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.id, self.question_text)

    def __unicode__(self):
        return

# Clase


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.id, self.choices_text)

    def __unicode__(self):
        return
