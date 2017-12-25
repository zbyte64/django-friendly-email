import unittest


from .converters import simple, markdown


class ConverterTests(unittest.TestCase):
    def test_simple(self):
        result = simple("<em>Hello</em> <i>World</i>")
        self.assertEqual(result, "Hello World")

    def test_markdown(self):
        result = markdown("<em>Hello</em> <i>World</i>")
        self.assertEqual(result, "_Hello_ _World_\n\n")
