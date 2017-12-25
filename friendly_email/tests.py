import unittest
from django.core.mail import EmailMessage, EmailMultiAlternatives

from .converters import simple, markdown
from .message import FriendlyEmail, patch_message


class ConverterTests(unittest.TestCase):
    def test_simple(self):
        result = simple("<em>Hello</em> <i>World</i>")
        self.assertEqual(result, "Hello World")

    def test_markdown(self):
        result = markdown("<em>Hello</em> <i>World</i>")
        self.assertEqual(result, "_Hello_ _World_\n\n")


class PatchMessageTests(unittest.TestCase):
    def test_add_alternative(self):
        message = EmailMultiAlternatives(
            'Hello',
            '<em>Body<em> goes here',
            'from@example.com',
            ['to1@example.com', 'to2@example.com'],
            ['bcc@example.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )
        patch_message(message)
        self.assertEqual(len(message.alternatives), 1)
        self.assertEqual(message.content_subtype, 'html')


class FriendlyEmailMessageTests(unittest.TestCase):
    def test_generate(self):
        message = FriendlyEmail(
            'Hello',
            '<em>Body<em> goes here',
            'from@example.com',
            ['to1@example.com', 'to2@example.com'],
            ['bcc@example.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )
        message.send()
        self.assertEqual(len(message.alternatives), 1)
