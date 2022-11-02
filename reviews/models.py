from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from restaurants.models import Restaurant
# Create your models here.

class GradeSelect(models.IntegerChoices):
    one = 1, '⭐'
    two = 2, '⭐⭐'
    three = 3, '⭐⭐⭐'
    four = 4, '⭐⭐⭐⭐'
    five = 5, '⭐⭐⭐⭐⭐'

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    grade = models.IntegerField(default=GradeSelect.five, choices=GradeSelect.choices)
    image = ProcessedImageField(
        upload_to="images/reviews_file/",
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 80},
    )
    thumbnail = ProcessedImageField(
        upload_to="images/reviews_file/",
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 60},
    )
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)