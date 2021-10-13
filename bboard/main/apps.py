from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Доска объявлений'


def user_registered():
    return None