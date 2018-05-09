from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "sudansite/homepage.html")


def history(request):
    return render(request, "sudansite/history.html")


def politics(request):
    return render(request, "sudansite/politics.html")


def culture(request):
    return render(request, "sudansite/culture.html")



