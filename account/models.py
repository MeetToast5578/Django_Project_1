from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import AbstractModel

# Create your models here.

class User(AbstractUser):
    phone = models.CharField('phone', max_length=50, null=True, blank=True)
    email = models.EmailField("email address")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    is_fake = models.BooleanField(default=False)
    
    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return '/static/images/profile/Basic_Profile_pic.jpg'


class Address(AbstractModel):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} address'

class BlockedIpAddress(AbstractModel):
    ip_address = models.GenericIPAddressField()
        
