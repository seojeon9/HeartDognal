from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    tel = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    addr = models.CharField(max_length=300, blank=True)
    addr_detail = models.CharField(max_length=300, blank=True)





