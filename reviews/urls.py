from django.urls import path
from . import views
from reviews.views import ReviewsView
app_name = "reviews"

urlpatterns = [
    path('', ReviewsView.as_view(), name="reviews"),
    path("", views.index, name="index"),
    path("<int:pk>", views.detail, name="detail"),
    path("<int:restaurant_pk>/create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path(
        "<int:pk>/comments/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
]
