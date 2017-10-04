import requests
import datetime
from django.shortcuts import render


def index(request):
    posts = requests.get("http://127.0.0.1:8001/api/1.0/posts/?status=2")
    tags = requests.get("http://127.0.0.1:8001/api/1.0/tags/")

    context = {
        'posts': posts.json()['results'],
        'tags': tags.json()['results']
    }
    return render(request, "blogs/index.html", context)


def detail(request):
    
    return render(request, "blogs/detail.html")


def PostByCategory(request, tag_pk):
    params = {'status': '2', 'tag_pk': tag_pk}
    tag = requests.get(
        "http://127.0.0.1:8001/api/1.0/tags/"+tag_pk+"/")
    posts = requests.get(
        "http://127.0.0.1:8001/api/1.0/posts/", params=params)
    tags = requests.get("http://127.0.0.1:8001/api/1.0/tags/")
    
    print(tag.json())

    context = {
        'posts': posts.json()['results'],
        'tags': tags.json()['results'],
        'tag': tag.json()
    }
    return render(request, "blogs/post_by_category.html", context)


def login(request):
    return render(request, "login.html")


def singin(request):
    return render(request, "singin.html")

