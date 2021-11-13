from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):    
    detail = models.TextField(max_length=1000, blank=True)