from django.shortcuts import render


def index(request):
    return render(request, "blogs/index.html")


def detail(request):
    return render(request, "blogs/detail.html")


def PostByCategory(request):
    return render(request, "blogs/post_by_category.html")
