from setuptools import setup

setup(
    name="django-querycount",
    version="0.1.0",
    author="Smith Krengkrud",
    author_email="smith.kre@gmail.com",
    description=("Allow you to login to any user via django command."),
    install_requires=[],
    license="BSD 3",
    keywords="django dev admin helper",
    url="https://github.com/smithkre/django-dev-admin",
    packages=[
        "django_dev_admin",
    ],
    long_description="This project gives you a middleware that allow you to login to any user via django command.",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Utilities",
    ],
)