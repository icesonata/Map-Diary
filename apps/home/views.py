from django.shortcuts import render

# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     print(request.user.profile.profile_url)
    username = request.user.username
    context = {"username": username}
    return render(request, "home/home.html", context)