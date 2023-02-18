release: python src/manage.py migrate; python src/manage.py build_verbs
web: gunicorn tagalogverbs.wsgi --log-file -
