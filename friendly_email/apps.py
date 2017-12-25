from django.apps import AppConfig
from django.conf import settings
from django.core.mail.message import EmailMessage, EmailMultiAlternatives

from .message import FriendlyEmail
from .converters import CONVERTER


class FriendlyEmailConfig(AppConfig):
    name = 'friendly_email'
    verbose_name = "Friendly Email"

    def ready(self):
        if getattr(settings, 'FRIENDLY_EMAIL_MONKEY_PATCH', False):
            if 'anymail' in settings.INSTALLED_APPS:
                from anymail.signals import pre_send
                pre_send.connect(patch_anymail_signal)
            else:
                pass #TODO monkey patch django


def patch_anymail_signal(message, esp_name, **kwargs):
    if isinstance(message, FriendlyEmail):
        return
    if isinstance(message, EmailMultiAlternatives):
        if message.alternatives:
            #alternatives already defined
            return
        message.attach_alternative(CONVERTER(message.body), 'text/plain')
        return
    if isinstance(message, EmailMessage):
        pass #can we upcast?
