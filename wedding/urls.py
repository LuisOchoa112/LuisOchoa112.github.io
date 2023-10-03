from django.urls import path
from . import views

app_name = "wedding"
urlpatterns = [
    path("", views.index, name="index"),
    path("RSVP", views.reserve, name="RSVP")
]