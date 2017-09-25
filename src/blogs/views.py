from django.shortcuts import render


def index(request):
    return render(request, "blogs/list.html")


def detail(request):
    return render(request, "blogs/detail.html")


def login(request):
    return render(request, "login.html")


def singin(request):
    return render(request, "singin.html")
