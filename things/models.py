from django.db import models

class Thing(models.Model):
    name = models.CharField()
    desciption = models.CharField()
    quantity = models.IntegerField()