"""
It is a configuration file common to all Django apps
"""
from django.apps import AppConfig


class SmtpAppConfig(AppConfig):
    """
     It is a configuration file common to all Django apps
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_send'
