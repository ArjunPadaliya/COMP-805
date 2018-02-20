from django.db import models
from datetime import date
# Create your models here.

class Resume(models.Model):
    first_name=models.CharField(max_length=64, null=False, blank=False)
    last_name=models.CharField(max_length=64, null=False, blank=False)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def last_name_first_name(self):
        return "{}, {}".format(self.last_name, self.first_name)

    def get_experience(self):
        return self.experience_set.all()

    def get_education(self):
        return self.education_set.all()

class Experience(models.Model):
    parent_resume=models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    title=models.CharField(max_length=64, null=True, blank=False)
    location=models.CharField(max_length=64, null=True, blank=False)
    start_date=models.DateField(blank=True, null=True)
    end_date=models.DateField(blank=True, null=True)
    description=models.CharField(max_length=256, null=False, blank= True)

    def __str__(self):
        return self.title


class Education(models.Model):
    parent_resume=models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    institution_name=models.CharField(max_length=256, null=True, blank=False)
    location=models.CharField(max_length=64, null=True, blank=False)
    degree=models.CharField(max_length=64, null=True, blank=False)
    major=models.CharField(max_length=64, null=True, blank=False)
    gpa=models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.institution_name
