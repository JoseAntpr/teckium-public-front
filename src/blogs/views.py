import requests
import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse

from blogs.decorators import jwt_required
from blogs.requests_api import get_posts, get_tags, get_post, get_comments, create_comment, get_blogs, create_post, delete_comment, \
    put_post, delete_post
from users.requests_api import tk_refresh
from blogs.forms import CommentForm, PostForm


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
        params = {'status': 2}
        posts = get_posts(params)
        tags = get_tags()

        context = {
            'posts': posts['results'],
            'tags': tags['results'],
            'next': posts['next'],
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
       
        context = {
            'post': post,
            'tags': tags['results'],
            'user': user,
            'comments': comments['results'],
            'next': comments['next'],
            'form':  CommentForm()
        }

        if new_token:
            request.session["jwt"] = new_token

        return render(request, "blogs/detail.html", context)

    def post(self, request, blog_pk, post_pk):
        form = CommentForm(request.POST)
        token = request.session.get('jwt', None)
        user = []
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']

        if form.is_valid():
            data = {'content': form.cleaned_data.get('content'),
                    'owner.username': user.get('username'),
                    'post': post_pk}
            create_comment(data)

        params = {"post": post_pk}
        post = get_post(post_pk)
        tags = get_tags()
        comments = get_comments(params)
        
        context = {
            'post': post,
            'tags': tags['results'],
            'user': user,
            'comments': comments['results'],
            'next': comments['next'],
            'form':  CommentForm()
        }
            
        return render(request, "blogs/detail.html", context)


class DeleteComment(View):
    @method_decorator(jwt_required)
    def get(self, request, blog_pk, post_pk, comment_pk):
        delete_comment(comment_pk)
        return HttpResponseRedirect(reverse('post-detail', args=[blog_pk, post_pk]))

        
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


class NewBlogView(View):
    @method_decorator(jwt_required)
    def get(self, request, **kwargs):
        user = kwargs['user']
        token = kwargs['token']
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']
                request.session["jwt"] = new_token
        tags = get_tags()
        params = {'owner': user.get('id')}
        blogs = get_blogs(params)

        context = {
            'tags': tags['results'],
            'user': user,
            'form': PostForm(tags=tags['results'], blogs=blogs['results'])
        }

        return render(request, "blogs/new-blog.html", context)
    
    @method_decorator(jwt_required)
    def post(self, request, **kwargs):
        user = kwargs['user']
        token = kwargs['token']
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']
                request.session["jwt"] = new_token
        
        params = {'owner': user.get('id')}
        blogs = get_blogs(params)
        tags = get_tags()
        
        form = PostForm(request.POST, request.FILES, tags=tags['results'], blogs=blogs['results'])

        if form.is_valid():
            file = { 
                'image': form.cleaned_data.pop('image')
            }
            data = {
                'owner': user.get('id'),
                'tags': form.cleaned_data.get('tags'),
                'title': form.cleaned_data.get('title'),
                'summary': form.cleaned_data.get('summary'),
                'content': form.cleaned_data.get('content'),
                'status': 2 if 'publish' in request.POST else 1,
                'blog': form.cleaned_data.get('blogs')

            }
            create_post(file, data)
            return redirect('index')

        context = {
            'tags': tags['results'],
            'user': user,
            'form': PostForm(tags=tags['results'], blogs=blogs['results'])
        }
        return render(request, "blogs/new-blog.html", context)


class EditPostView(View):
    @method_decorator(jwt_required)
    def get(self, request, post_pk, **kwargs):
        user = kwargs['user']
        token = kwargs['token']
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']
                request.session["jwt"] = new_token

        tags = get_tags()
        params = {'owner': user.get('id')}
        blogs = get_blogs(params)
        post = get_post(post_pk)

        context = {
            'tags': tags['results'],
            'post': post,
            'user': user,
            'form': PostForm(post, tags=tags['results'], blogs=blogs['results'])
        }

        return render(request, "blogs/edit-blog.html", context)

    @method_decorator(jwt_required)
    def post(self, request, post_pk, **kwargs):
        user = kwargs['user']
        token = kwargs['token']
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']
                request.session["jwt"] = new_token

        params = {'owner': user.get('id')}
        blogs = get_blogs(params)
        post = get_post(post_pk)
        tags = get_tags()

        form = PostForm(request.POST, request.FILES, tags=tags['results'], blogs=blogs['results'])

        if form.is_valid():
            file = {
                'image': form.cleaned_data.pop('image')
            }
            data = {
                'owner': user.get('id'),
                'tags': form.cleaned_data.get('tags'),
                'title': form.cleaned_data.get('title'),
                'summary': form.cleaned_data.get('summary'),
                'content': form.cleaned_data.get('content'),
                'status': 2 if 'publish' in request.POST else 1,
                'blog': form.cleaned_data.get('blogs')

            }
            put_post(post_pk, file, data)
            return HttpResponseRedirect(reverse('post-detail', args=[post.get('blog').get('id'), post_pk]))

        context = {
            'tags': tags['results'],
            'user': user,
            'form': PostForm(tags=tags['results'], blogs=blogs['results'])
        }
        return render(request, "blogs/edit-blog.html", context)


class DeletePost(View):
    @method_decorator(jwt_required)
    def get(self, request, post_pk, **kwargs):

        user = kwargs['user']
        token = kwargs['token']
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                user = data['user']
                new_token = data['token']
                request.session["jwt"] = new_token

        delete_post(post_pk)

        params = {'status': 2}
        posts = get_posts(params)
        tags = get_tags()

        context = {
            'posts': posts['results'],
            'tags': tags['results'],
            'next': posts['next'],
            'user': user
        }

        if new_token:
            request.session["jwt"] = new_token

        return render(request, "blogs/index.html", context)

