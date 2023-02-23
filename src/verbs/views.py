import random

from django.shortcuts import render
from rest_framework import viewsets


from . import models, serializers

import logging

logger = logging.getLogger(__name__)

PRONOUNS = [
    ("I", "ako"),
    ("you", "ka"),
    ("he/she", "siya"),
    ("we", "kami/tayo"),
    ("you guys", "kila"),
    ("they", "sila"),
]

VERBCOUNT = 72


class VerbViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Verb.objects.all()
    serializer_class = serializers.VerbSerializer


def home(request):
    return render(request, "verbs/home.html", {})


def randomizer(request):
    random_pk = random.randint(1, VERBCOUNT)
    random_verb = models.Verb.objects.get(id=random_pk)
    english = random_verb.english

    possible_answers = models.Verb.objects.filter(english=english).all()
    return render(
        request,
        "verbs/randomizer.html",
        {"random_verb": random_verb, "possible_answers": possible_answers},
    )


def about(request):
    return render(request, "verbs/about.html", {})


def conjugation(request, verb_pk):
    verb = models.Verb.objects.get(id=verb_pk)
    BASE_URL = "http://www.wordreference.com/conj/FrVerbs.aspx?v={}"
    verb_url = BASE_URL.format(verb.root)

    pronoun = random.choice(PRONOUNS)
    return render(
        request,
        "verbs/conjugation.html",
        {"pr": pronoun, "verb": verb, "verb_url": verb_url},
    )


def memorize(request):
    ids = [random.randint(1, VERBCOUNT) for _ in range(1, 21)]
    verbs = models.Verb.objects.filter(id__in=ids)
    return render(request, "verbs/memorize.html", {"verbs": verbs})
