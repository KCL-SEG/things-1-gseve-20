from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=40)
    desciption = models.CharField(max_length=400)
    quantity = models.IntegerField()