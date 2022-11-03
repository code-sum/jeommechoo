from django import forms
from .models import Review, Comment



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'restaurant',
            "content",
            "image",
            "grade",
        ]
        labels = {
            'restaurant': '식당 이름', 
            'content': '리뷰내용', 
            'image': '메뉴 사진', 
            'grade': '평점', 
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]