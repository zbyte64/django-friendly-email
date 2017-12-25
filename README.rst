Django Friendly Email generates text alternative emails for you.
Write your email templates as HTML and let this library worry about plain text email so you don't have to.

For best results also install `django-anymail` and `html2text`



Settings
========

FRIENDLY_EMAIL_MONKEY_PATCH
  is false by default.
  Set to True to patch messages as they are sent.
  Setting this to ``anymail`` will use anymail's signals instead of monkey patching code.

FRIENDLY_EMAIL_CONVERTER
  is ``friendly_email.converters.simple`` by default.
  ``friendly_email.converters.markdown`` requires html2text to be installed.


API
===


``friendly_email.message.FriendlyEmail`` is a Django Email class that will automatically generate a text alternative.

``friendly_email.message.patch_message`` will add a text alternative to an existing `EmailMultiAlternatives` object.
