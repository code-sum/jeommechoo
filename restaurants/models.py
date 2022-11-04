from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.translation import gettext_lazy as _

class CategorySelect(models.IntegerChoices):
    one = 1, '한식'
    two = 2, '중식'
    three = 3, '프렌치'
    four = 4, '이탈리안'
    five = 5, '스페니쉬'
    six = 6, '아메리칸'
    seven = 7, '튀르키예'
    eight = 8, '디저트'
    nine = 9, '멕시칸'
    ten = 10, '최준홍님 pick!'
    eleven = 11, '일식'

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    menupan = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_restaurants')
    category = models.IntegerField(default=CategorySelect.ten, choices=CategorySelect.choices)
    image = ProcessedImageField(upload_to='images/restaurant/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
    thumbnail = ProcessedImageField(upload_to='images/restaurant/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
    def __str__(self):
        return self.name