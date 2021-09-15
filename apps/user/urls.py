from django.contrib import auth
from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LogoutView
from .views import CustomRegisterView, CustomLoginView

# app_name = "user"
urlpatterns = [
    # path("register", views.register, name="register"),
    # path("login", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    # path("logout", auth_views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path('register', CustomRegisterView.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]