from django import forms
from .models import Review, Comment



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "content",
            "image",
            "grade",
        ]
        labels = {
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