from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("juliano", views.juliano, name = "juliano"),
    path("<str:name>", views.greet, name = "greet")
]
