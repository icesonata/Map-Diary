from django.shortcuts import render
from apps.user.models import UserProfile

# Create your views here.
def index(request):
    return render(request, "home/home.html")