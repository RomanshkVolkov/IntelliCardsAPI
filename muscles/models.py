from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=255)
    insertion = models.CharField(max_length=255)
    innervation = models.CharField(max_length=255)
    action = models.CharField(max_length=255)


    class Meta:
        db_table = 'muscles'
