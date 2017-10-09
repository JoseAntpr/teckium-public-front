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

from blogs.views import IndexView, DetailView, PostByCategoryView
from users.views import LoginView, SigninView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^$', index, name="index"),
    url(r'^(?P<blog_pk>[0-9]+)/(?P<post_pk>[0-9]+)', detail.as_view(),
        name="post-detail"),
    url(r'^tag/(?P<tag_pk>[0-9]+)$', PostByCategory, name="posts-tag"),
=======
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^detail', DetailView.as_view(), name="post-detail"),
    url(r'^tag/(?P<tag_pk>[0-9]+)$', PostByCategoryView.as_view(), name="posts-tag"),
>>>>>>> d19782e05c54691ef6dfa57b337fc902d2d27326

    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^signin', SigninView.as_view(), name="signin"),
    url(r'^logout', LogoutView.as_view(), name="logout"),

]
