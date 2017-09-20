from django.shortcuts import render


def index(request):
    return render(request, "blogs/list.html")


def detail(request):
    return render(request, "blogs/detail.html")
