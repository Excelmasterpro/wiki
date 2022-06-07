from django.urls import path

from unicodedata import name
from django.urls import URLPattern

from . import views

app_name = "wikiNC"

urlpatterns = [
    path("", views.index, name="index"),
    #  path("entry", views.entry, name="entry")
    path('Wiki/<str:title>', views.entry, name="entry"),
    path('search', views.search, name="search")
 
]
