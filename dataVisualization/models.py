from django.db import models

# Create your models here.
class Company(models.Model):
    end_year = models.CharField(max_length=10,default="")
    start_year = models.CharField(max_length=10,default="")
    intensity = models.IntegerField(default=0)
    sector = models.CharField(max_length=100,default="")
    topic = models.CharField(max_length=100,default="")
    region = models.CharField(max_length=100,default="")
    country = models.CharField(max_length=100,default="")
    relevance = models.IntegerField(default=0)
    pestle = models.CharField(max_length=50,default="")
    source = models.CharField(max_length=50,default="")
    likelihood = models.IntegerField(default=0)

    title = models.CharField(max_length=800,default="")
    published = models.CharField(max_length=100,default="")
    added = models.CharField(max_length=100,default="")
    impact = models.CharField(max_length=100,default="")
    url = models.URLField(max_length=400,default="")
    insight = models.CharField(max_length=500,default="")
