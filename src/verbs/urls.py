from django.conf.urls import include
from django.urls import re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'verbs', views.VerbViewSet)


urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^randomizer", views.randomizer, name="randomizer"),
    re_path(r"^about", views.about, name="about"),
    re_path(r"^conjugation/(?P<verb_pk>\d+)/$", views.conjugation, name="conjugation"),
    re_path(r"^memorize", views.memorize, name="memorize"),
    re_path("api/", include(router.urls)),
]
