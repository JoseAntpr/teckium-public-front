import requests
import datetime
from django.shortcuts import render

from teckiumDjangoFront.settings import INFO_API


def index(request):
    #posts = requests.get(INFO_API.get("url") + INFO_API.get("version") + "posts/?status=2")
    posts = requests.get(INFO_API.get("url") + INFO_API.get("version") + "posts/")
    tags = requests.get(INFO_API.get("url") + INFO_API.get("version") + "tags/")

    context = {
        'posts': posts.json()['results'],
        'tags': tags.json()['results']
    }
    return render(request, "blogs/index.html", context)


def detail(request):
    return render(request, "blogs/detail.html")


def PostByCategory(request, tag_pk):
    #params = {'status': '2', 'tags': tag_pk}
    params = {'tags': tag_pk}
    tag = requests.get(
        INFO_API.get("url") + INFO_API.get("version") + "tags/"+tag_pk+"/")
    posts = requests.get(
        INFO_API.get("url") + INFO_API.get("version") + "posts/", params=params)
    tags = requests.get(INFO_API.get("url") + INFO_API.get("version") + "tags/")

    context = {
        'posts': posts.json()['results'],
        'tags': tags.json()['results'],
        'tag': tag.json()
    }
    return render(request, "blogs/post_by_category.html", context)
