import requests
import datetime
from django.shortcuts import render
from django.views import View

from blogs.requests_api import get_posts, get_tags
from teckiumDjangoFront.settings import INFO_API


class IndexView(View):

    def get(self, request):
        # posts = requests.get(INFO_API.get("url") + INFO_API.get("version") + "posts/?status=2")
        params = {}
        posts = get_posts(params)
        tags = get_tags()

        context = {
            'posts': posts['results'],
            'tags': tags['results']
        }
        return render(request, "blogs/index.html", context)


class DetailView(View):

    def get(self, request):
        return render(request, "blogs/detail.html")


class PostByCategoryView(View):

    def get(self, request, tag_pk):
        #params = {'status': '2', 'tags': tag_pk}
        params = {'tags': tag_pk}
        tag = get_tags(tag_pk)
        posts = get_posts(params)
        tags = get_tags()

        context = {
            'posts': posts['results'],
            'tags': tags['results'],
            'tag': tag
        }
        return render(request, "blogs/post_by_category.html", context)
