"""teckiumDjangoFront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blogs.views import IndexView, DetailView, PostByCategoryView, NewBlogView ,DeleteComment, EditPostView, DeletePost
from users.views import LoginView, SigninView, LogoutView, ProfileView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<blog_pk>[0-9]+)/(?P<post_pk>[0-9]+)/$', DetailView.as_view(),
        name="post-detail"),
    url(r'^tag/(?P<tag_pk>[0-9]+)$', PostByCategoryView.as_view(), name="posts-tag"),
    url(r'^new-post', NewBlogView.as_view(), name="new-post"),
    url(r'^edit-post/(?P<post_pk>[0-9]+)$', EditPostView.as_view(), name="edit-post"),
    url(r'^(?P<blog_pk>[0-9]+)/(?P<post_pk>[0-9]+)/delete-comment/(?P<comment_pk>[0-9]+)', DeleteComment.as_view(), name="delete-comment"),
    url(r'^delete-post/(?P<post_pk>[0-9]+)$', DeletePost.as_view(), name="delete-post"),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^signin', SigninView.as_view(), name="signin"),
    url(r'^logout', LogoutView.as_view(), name="logout"),
    url(r'^profile', ProfileView.as_view(), name="profile"),
]
