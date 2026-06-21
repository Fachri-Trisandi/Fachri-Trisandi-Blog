from django.urls import path

from . import views

app_name = "materi"

urlpatterns = [
    path("", views.index, name="index"),
    path("materi/<slug:slug>/", views.detail, name="detail"),
]
