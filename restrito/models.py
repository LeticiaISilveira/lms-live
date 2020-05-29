from django.db import models


class Curso(models.Model):

    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=5, unique=True)
