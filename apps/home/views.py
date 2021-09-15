from django.shortcuts import render

# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    username = request.user.username
    context = {"username": username}
    return render(request, "home/home.html", context)