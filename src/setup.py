from setuptools import setup, find_packages

setup(
    name = "todoapp",
    version = "0.1.0",
    description = "Todo backend Django REST service",
    packages = find_packages(),
    include_package_data = True,
    scripts = ["manage.py"],
    install_requires = [
        "Django>=1.11.1,<1.12",
        "django-cors-headers>=2.0.2",
        "djangorestframework>=3.6.2",
        "MySQL-python>=1.2.5",
        "uwsgi>=2.0",
    ],
    extras_require = {
        "test": [
            "colorama>=0.3.9",
            "coverage>=4.3.4",
            "django-nose>=1.4.4",
            "nose>=1.3.7",
            "pinocchio>=0.4.2",
        ],
    },
)
