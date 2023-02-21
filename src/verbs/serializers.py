from rest_framework import serializers

from .models import Verb


class VerbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Verb
        fields = "__all__"
