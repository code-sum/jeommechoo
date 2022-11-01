from django.urls import path
from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index')
]