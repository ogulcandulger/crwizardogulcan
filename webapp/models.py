from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):    
    detail = models.TextField(max_length=1000, blank=True)

class XML(models.Model):
    user = models.ForeignKey( MyUser, on_delete=models.CASCADE )
    xml_link = models.CharField(max_length=250)
    xml_file = models.FileField(upload_to='', max_length=500, blank=True)
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.xml_link