from django.db import models
import os
from django.db import models
from django.conf import settings

# Create your models here.
class gamedata(models.Model):
    id=models.IntegerField(primary_key=True)
    data=models.ImageField(upload_to='gamedata/')

  
