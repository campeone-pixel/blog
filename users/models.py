

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    image_thumbnail = ImageSpecField(source='image',
                                  processors=[ResizeToFill(50, 50)],
                                  format='JPEG',
                                  options={'quality': 100})
    image_profile = ImageSpecField(source='image',
                                  processors=[ResizeToFill(200, 200)],
                                  format='JPEG',
                                  options={'quality': 100})


    def __str__(self):
        return f'{self.user.username} Profile' 
    
    
