from importlib.metadata import requires
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Technologie(models.Model):
    name =  models.CharField(max_length=20, unique=True, null=False, blank=False)
    TYPE = (('F', 'Front-end'), ('B', 'Back-end'), ('FS', 'Full-stack'))
    type_technologie = models.CharField(max_length=2, null=False, choices=TYPE)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    describe = models.TextField(null=False)
    date_init = models.DateField()
    date_end = models.DateField()
    concluid_project = models.BooleanField(default=False)
    technologie = models.ForeignKey(Technologie, on_delete=models.CASCADE)

    def __str__(self):
        return self.describe
