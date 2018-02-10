from django.db import models
from datetime import date
# Create your models here.

class Experience(models.Model):
    title=models.CharField(max_length=64, null=True, blank=False)
    location=models.CharField(max_length=64, null=True, blank=False)
    start_date=models.DateField(blank=True, null=True)
    end_date=models.DateField(blank=True, null=True)
    description=models.CharField(max_length=256, null=False, blank= True)

class Education(models.Model):
    institution_name=models.CharField(max_length=256, null=True, blank=False)
    location=models.CharField(max_length=64, null=True, blank=False)
    degree=models.CharField(max_length=64, null=True, blank=False)
    major=models.CharField(max_length=64, null=True, blank=False)
    gpa=models.FloatField(null=True, blank=True)
