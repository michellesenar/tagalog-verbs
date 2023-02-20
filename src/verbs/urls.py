from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^randomizer", views.randomizer, name="randomizer"),
    re_path(r"^about", views.about, name="about"),
    re_path(r"^conjugation/(?P<verb_pk>\d+)/$", views.conjugation, name="conjugation"),
    re_path(r"^memorize", views.memorize, name="memorize"),
]
