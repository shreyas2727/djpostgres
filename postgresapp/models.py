from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    added_date = models.DateField(auto_now_add=True)

    