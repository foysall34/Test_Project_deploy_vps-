from django.db import models
from django.conf import settings
# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
   




