from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_safe

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@require_safe
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('main')
        else:
            form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('accounts:detail')