from django.db import models


class Verb(models.Model):
    id = models.AutoField(primary_key=True)
    english = models.CharField(max_length=40)
    root = models.CharField(max_length=40)
    root_ascii = models.CharField(max_length=40)
    actor_past = models.CharField(max_length=40, default="")
    actor_present = models.CharField(max_length=40, default="")
    actor_future = models.CharField(max_length=40, default="")
