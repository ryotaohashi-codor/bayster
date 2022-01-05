from django.db import models

# Create your models here.

class Land(models.Model):
    title = models.CharField(max_length=40)