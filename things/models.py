from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    desciption = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])