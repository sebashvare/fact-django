from django.db import models

"""
================================================
        Creacion Modelos de la APP 
        Questions, Choices
================================================
"""

# Clase Question


class Question(models.Model):

    question_text = models.CharField(
        max_length=200,
        help_text="Ingresa la pregunta")

    pub_date = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.question_text, self.pub_date)

    def __unicode__(self):
        return

# Clase


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return

    def __unicode__(self):
        return
