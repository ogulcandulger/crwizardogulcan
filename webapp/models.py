from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):    
    detail = models.TextField(max_length=1000, blank=True)

class XML(models.Model):
    user = models.ForeignKey( MyUser, on_delete=models.CASCADE )
    xml_link = models.CharField(max_length=250)

    def __str__(self):
        return self.name