from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):            # connects signals with the app
        import account.signals 