from django.db import models

class Abs(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)

    class Meta:
        db_table = 'abdominales'

class Biceps(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)

    class Meta:
        db_table = 'biceps'

class Hombros(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)

    class Meta:
        db_table = 'hombros'

class Pecho(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)

    class Meta:
        db_table = 'pecho'

class Piernas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)

    class Meta:
        db_table = 'piernas'
