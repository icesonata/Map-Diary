from django.urls import path
from . import views

app_name = "memory"
urlpatterns = [
    path("create", views.create, name="memory_create"),
    path("detail/<str:id>", views.detail, name="memory_detail"),
]