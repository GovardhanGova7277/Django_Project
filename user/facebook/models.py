from django.db import models

# Create your models here.


class User(models.Model):
    names = models.CharField(max_length=30)
    emails = models.CharField(max_length=30, unique=True)
    passwords = models.CharField(max_length=30)
