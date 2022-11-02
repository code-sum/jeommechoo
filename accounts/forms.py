from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'profileimg')
        labels = {'username': '아이디', 'password1': '비밀번호', 'password2': '비밀번호 확인','profileimg': '프로필 이미지',
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('last_name',)
        labels = {'last_name': '유저소개',
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=("새 비밀번호"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=None
        )
