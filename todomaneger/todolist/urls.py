
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "todolist"

urlpatterns = [
    path("", views.vid_view, name="vid"),
    path("<int:pk>/", views.ToDoDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.ToDoItemUpdateView.as_view(), name="update"),
    path("<int:pk>/confirm-delete", views.ToDoItemDeleteView.as_view(), name="delete"),
    path("create/", views.ToDoItemCreateView.as_view(), name="create"),
]
