import requests
from django.shortcuts import render


def index(request):
    blogs = requests.get("http://127.0.0.1:8001/api/1.0/blogs/")

    context = {
        'blogs': blogs.json()['results']
    }
    return render(request, "blogs/index.html", context)


def detail(request):
    return render(request, "blogs/detail.html")


def PostByCategory(request):
    return render(request, "blogs/post_by_category.html")


def login(request):
    return render(request, "login.html")


def singin(request):
    return render(request, "singin.html")
