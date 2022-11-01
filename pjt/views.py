from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def main(request):
    forms = AuthenticationForm()
    context = {
        'forms' : forms,
    }
    return render(request, "main.html", context)