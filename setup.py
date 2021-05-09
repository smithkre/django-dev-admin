from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-dev-admin",
    version="1.0.1",
    author="Smith Krengkrud",
    author_email="smith.kre@gmail.com",
    description=(
        "A Django app to help developers login to any user via django command."
    ),
    install_requires=[],
    license="BSD 3",
    keywords="django dev admin helper",
    url="https://github.com/smithkre/django-dev-admin",
    packages=[
        "django_dev_admin",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Utilities",
    ],
)