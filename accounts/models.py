from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profileimg = ProcessedImageField(upload_to='images/profile/', blank=True,
                                processors=[ResizeToFill(100, 100)],
                                format='JPEG',
                                options={'quality': 80})