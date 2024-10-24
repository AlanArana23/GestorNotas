from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=50)
    content = models.TextField()
    creation_date = models.DateTimeField("Creacion de una nota", auto_now_add=True)


    def __str__(self):
        return self.title