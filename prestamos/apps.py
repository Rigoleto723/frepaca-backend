from django.apps import AppConfig


class PrestamosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prestamos'

    def ready(self):
        import prestamos.signals
