from django.apps import AppConfig


class LogusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logusers'

    def ready(self):
        import logusers.signals
