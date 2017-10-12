import requests
import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from blogs.requests_api import get_posts, get_tags, get_post, get_comments
from users.requests_api import tk_refresh


class IndexView(View):
    def get(self, request):
        token = request.session.get("jwt", None)
        user = []
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']

        # posts = requests.get(INFO_API.get("url") + INFO_API.get("version") + "posts/?status=2")
        params = {}
        posts = get_posts(params)
        tags = get_tags()

        context = {
            'posts': posts['results'],
            'tags': tags['results'],
            'user': user
        }

        if new_token:
            request.session["jwt"] = new_token

        return render(request, "blogs/index.html", context)


class DetailView(View):
    def get(self, request, blog_pk, post_pk):
        token = request.session.get("jwt", None)
        user = []
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']

        # posts = requests.get(INFO_API.get("url") + INFO_API.get("version") + "posts/?status=2")
        params = {"post": post_pk}
        post = get_post(post_pk)
        tags = get_tags()
        comments = get_comments(params)
        print(comments['results'])

        context = {
            'post': post,
            'tags': tags['results'],
            'user': user,
            'comments': comments['results']
        }

        if new_token:
            request.session["jwt"] = new_token

        return render(request, "blogs/detail.html", context)


class PostByCategoryView(View):
    def get(self, request, tag_pk):
        token = request.session.get("jwt", None)
        user = []
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']

        # params = {'status': '2', 'tags': tag_pk}
        params = {'tags': tag_pk}
        tag = get_tags(tag_pk)
        posts = get_posts(params)
        tags = get_tags()

        context = {
            'posts': posts['results'],
            'tags': tags['results'],
            'user': user,
            'tag': tag
        }

        if new_token:
            request.session["jwt"] = new_token

        return render(request, "blogs/post_by_category.html", context)
