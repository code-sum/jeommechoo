from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone', 'menupan', 'category', 'thumbnail', 'image']
        labels = {
            'name': '식당 이름', 
            'address': '주소', 
            'phone': '전화번호', 
            'menupan': '메뉴', 
            'category': '분류', 
            'thumbnail' : '식당 외관 사진', 
            'image': '추가 이미지'
        }