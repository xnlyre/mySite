from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.


class Room(models.Model):
    name = CharField(max_length=200)
    description = TextField(max_length=1200)
    
    