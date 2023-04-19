from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=255)
    insertion = models.CharField(max_length=255)
    innervation = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    class Meta:
        db_table = 'muscles'

class Folder(models.Model):
    name = models.CharField(max_length=100)
    muscles = models.ManyToManyField(Muscle)

    class Meta:
        db_table = 'folders'

    def __str__(self):
        return self.name

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    folders = models.ManyToManyField(Folder)

    class Meta:
        db_table = 'custom_users'

    def __str__(self):
        return self.email
