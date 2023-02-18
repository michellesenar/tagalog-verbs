import csv
import unicodedata

from django.core.management.base import BaseCommand

from verbs.models import Verb

real_file = "tagalog-um-verbs.csv"


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(real_file, "r") as fp:
            reader = csv.reader(fp)
            for row in reader:
                english = row[0]
                print(english)
                target = row[1]
                print(target)
                for english_word in english.split(","):
                    nfkd_form = unicodedata.normalize("NFKD", target)
                    root_ascii = nfkd_form.encode("ASCII", "ignore")
                    fv = Verb()
                    fv.english = english_word
                    fv.root = target
                    fv.root_ascii = root_ascii
                    fv.save()
