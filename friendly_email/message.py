from django.core.mail import EmailMultiAlternatives

from .message import CONVERTER


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
