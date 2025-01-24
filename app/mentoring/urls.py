from django.urls import path

from . import views

app_name = "mentoring"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("profile/", views.MyProfileView.as_view(), name="my_profile"),
]
