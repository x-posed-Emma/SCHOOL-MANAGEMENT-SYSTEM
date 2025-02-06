from django.apps import AppConfig


class SmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SMS_APP'

    def ready(self):
        import SMS_APP.signals

 