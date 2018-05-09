"""sudansite URL Configuration
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('newsfeed/', include('newsfeed.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('history/', views.history, name="history"),
    path('politics/', views.politics, name="politics"),
    path('culture/', views.culture, name="culture"),
    path('newsfeed/', include("newsfeed.urls", namespace="newsfeed")),
    path('questions/', include("questions.urls", namespace="questions")),
    path('map/', include("map.urls", namespace="map")),
]
