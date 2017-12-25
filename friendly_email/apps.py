from django.apps import AppConfig
from django.conf import settings
from django.core.mail import get_connection

from .message import patch_message


class FriendlyEmailConfig(AppConfig):
    name = 'friendly_email'
    verbose_name = "Friendly Email"

    def ready(self):
        do_patch = getattr(settings, 'FRIENDLY_EMAIL_MONKEY_PATCH', False)
        if do_patch == 'anymail':
            from anymail.signals import pre_send
            pre_send.connect(patch_anymail_signal)
        elif do_patch:
            connection_klass = type(get_connection(fail_silently=True))
            connection_klass.send_messages = patch_send_messages(connection_klass.send_messages)


def patch_anymail_signal(message, **kwargs):
    patch_message(message)


def patch_send_messages(send_messages_fn):
    def send_messages(connection, messages):
        for message in messages:
            patch_messsage(message)
        return send_messages_fn(connection, messages)
    return send_messages
