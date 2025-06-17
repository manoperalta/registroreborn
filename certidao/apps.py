from django.apps import AppConfig


class CertidaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'certidao'

    def ready(self):
        import certidao.signals
