from django.urls import path 
from django.contrib.auth.decorators import login_required
from .views import MemoryCreate, MemoryDetail

app_name = "memory"
urlpatterns = [
    # require login before using service
    path('create', login_required(MemoryCreate.as_view()), name='memory_create'),
    path('detail/<int:pk>', login_required(MemoryDetail.as_view()), name='memory_detail'),
]