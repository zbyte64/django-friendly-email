from django.utils import strip_tags
from django.conf import settings
import importlib


DEFAULT_CONVERTER = getattr(settings, 'FRIENDLY_EMAIL_CONVERTER', 'friendly_email.converters.simple')


def simple(astr):
    return strip_tags(astr)


def markdown(astr):
    import html2text
    return html2text.html2text(astr)


_converter_module_name, _converter_fname = DEFAULT_CONVERTER.rsplit('.', 1)
_converter_module = importlib.import_module(_converter_module_name)
CONVERTER = getattr(_converter_module, _converter_fname)
