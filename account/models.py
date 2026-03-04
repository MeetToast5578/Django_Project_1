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
        

class BlockedIpAddress(AbstractModel):
    ip_address = models.GenericIPAddressField()
        
