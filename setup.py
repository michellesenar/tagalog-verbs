from setuptools import find_packages, setup

requirements = [
    "Django",
    "django-rest-framework",
    "gunicorn",
    "psycopg2",
    "python-dotenv",
    "whitenoise",
]

setup(
    name="tagalog-verbs",
    version="0.1",
    description="Practice Tagalog Verbs conjugation",
    url="https://github.com/michellesenar/tagalog-verbs",
    author="Michelle Senar Dressler",
    license="MIT",
    install_requires=requirements,
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": ["manage = manage:main"],
    },
)
