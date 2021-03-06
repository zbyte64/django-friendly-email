from django.core.mail import EmailMessage, EmailMultiAlternatives

from .converters import CONVERTER


class FriendlyEmail(EmailMultiAlternatives):
    '''
    Treat this as an HTML email and it will automatically generate a text alternative
    '''
    content_subtype = 'html'

    def has_text_alternative(self):
        for content, mimetype in self.alternatives:
            if mimetype in ('text', 'text/plain'):
                return True
        return False

    def generate_text_alternative(self):
        return CONVERTER(self.body)

    def send(self, fail_silently=False):
        if not self.has_text_alternative():
            self.attach_alternative(self.generate_text_alternative(), 'text/plain')
        return super(FriendlyEmail, self).send(fail_silently)


def patch_message(message):
    if isinstance(message, FriendlyEmail):
        return
    if isinstance(message, EmailMultiAlternatives):
        if message.alternatives:
            #alternatives already defined
            return
        message.attach_alternative(CONVERTER(message.body), 'text/plain')
        message.content_subtype = 'html'
        return
    if isinstance(message, EmailMessage):
        pass #can we upcast?
