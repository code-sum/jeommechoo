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
    content = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "100자 이내로 작성해주세요.",
        })
    )
    class Meta:
        model = Comment
        fields = [
            "content",
        ]