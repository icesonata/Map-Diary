from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def create(request):
    return render(request, "memory/create.html")

def detail(request, id):
    return render(request, "memory/detail.html")