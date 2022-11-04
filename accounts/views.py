from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomPasswordChangeForm,
)
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from restaurants.models import Restaurant
from reviews.models import Review
from restaurants.views import like
import requests



def reviewlist(request):
    users = get_user_model().objects.all()
    # user = get_user_model().objects.get(pk=)
    reviews = Review.objects.filter(
        id__in=users,
    ).values_list("user_id", flat=True)

    context = {
        "users": users,
        # "user": user,
        "reviews": reviews,
    }
    return render(request, "accounts/reviewlist.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("main")
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect("main")
        else:
            form = CustomUserCreationForm()
        context = {"form": form}
        return render(request, "accounts/signup.html", context)


@require_safe
def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    review = Review.objects.filter(user=user)
    like = Restaurant.objects.filter(like_users=user)
    like_restaurant = Restaurant.objects.filter(like_users=user).values('address')
    
    like_restaurant = [restaurant for restaurant in like_restaurant]
    client_id = '7apalzu8wx';    # 본인이 할당받은 ID 입력
    client_pw = 'LpKKb9dnZwQUKjkeDuXDZ6n3NgeD1uN50pvk9MYj';    # 본인이 할당받은 Secret 입력

    endpoint = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
   
    for restaurant in like_restaurant:

        url = f"{endpoint}?query={restaurant['address']}"

        headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id, 
        "X-NCP-APIGW-API-KEY": client_pw,
        }

        res = requests.get(url, headers=headers)

        lat = str(res.json()['addresses'][0]['y'])
        lng = str(res.json()['addresses'][0]['x'])

        restaurant['address'] = [lat, lng]

   
    context = {
        "user": user,
        "review":review,
        "like":like,
        "like_restaurant": like_restaurant,
    }

    return render(request, 'accounts/detail.html', context)


def login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect("main")
            else:
                messages.warning(request, "ID 또는 PASSWORD가 틀렸습니다.")
                return redirect("main")
    else:
        messages.warning(request, "ID 또는 PASSWORD가 틀렸습니다.")
        return redirect("main")


@login_required
def logout(request):
    auth_logout(request)
    return redirect("main")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("main")
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("main")


@require_POST
def follow(request, pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                "is_followed": is_followed,
                "followers_count": you.followers.count(),
                "followings_count": you.followings.count(),
            }
            return JsonResponse(context)
        return redirect("accounts:detail", you.username)
    return redirect("main")
