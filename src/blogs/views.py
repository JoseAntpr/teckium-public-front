import requests
from django.shortcuts import render


def index(request):
    posts = requests.get("http://127.0.0.1:8001/api/1.0/posts/")

    print(posts)

    context = {
        'posts': posts.json()['results']
    }
    return render(request, "blogs/index.html", context)


def detail(request):
    return render(request, "blogs/detail.html")


def PostByCategory(request):
    return render(request, "blogs/post_by_category.html")

