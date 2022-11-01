from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required

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

@login_required
def logout(request):
    auth_logout(request)
    return redirect('main')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('main')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
