from django.db import models

# Create your models here.
class Meal(models.Model):
    entree = models.CharField(max_length=100)
    appetizer = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
