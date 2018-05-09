from django.shortcuts import render
from .models import Region


def index(request):
    context = {'regions': Region.objects.all()}
    return render(request, "map/index.html", context)
