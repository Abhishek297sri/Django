from django.db import models


# Create your models here.
class Movie(models.Model):
    Mname = models.CharField(max_length=30)
    Dname = models.CharField(max_length=30)
    Hero = models.CharField(max_length=30)
    Heroine = models.CharField(max_length=30)
    Rdate = models.IntegerField()
    rating = models.FloatField()
