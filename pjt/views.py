from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from restaurants.models import Restaurant

def main(request):
    forms = AuthenticationForm()
    context = {
        'forms' : forms,
    }
    return render(request, "main.html", context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        restaurants = Restaurant.objects.filter(name__contains=searched)
        return render(request, 'searched.html', {'searched': searched, 'restaurants': restaurants})
    else:
        return render(request, 'searched.html', {})