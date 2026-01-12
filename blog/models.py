from django.db import models
from core.models import AbstractModel
# Create your models here.


class Comment(AbstractModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'Comment by {self.name}'