from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import CreateUserForm

# def register(request):
#     form = CreateUserForm()

#     if request.method == "POST":
#         form =CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get("username")
#             # messages.success(request, f'Account created for {username}!')
#             return redirect("/user/login")
#         # else:
#         #     messages.info(request, "Username or password is in correct")
#     else:
#         form = CreateUserForm()
#     context = {"form":form}
#     return render(request, "user/register.html", context)

class CustomRegisterView(CreateView):
    model = User
    template_name = "user/register.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')