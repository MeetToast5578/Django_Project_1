from django.db import models
from core.validators import validate_gmail

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):

    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200, null=True, blank=True)
    email = models.EmailField('Email', max_length=200, validators=[validate_gmail])
    message = models.TextField('Message')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'