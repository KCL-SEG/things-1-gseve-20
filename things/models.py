from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    desciption = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(min=0, max=100)