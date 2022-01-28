from unittest import TestCase
from unittest import skip

from .. import parse_md


class ParserTest(TestCase):

    def test_parse_h1(self):
        text = '# Title being tested'
        expected = '<h1>Title being tested</h1>'
        self.assertEqual(parse_md.parse_h1(text), expected)

    def test_parse_h1_on_multiple_lines(self):
        text = '# Title being tested\nsome more text'
        expected = '<h1>Title being tested</h1>some more text'
        self.assertEqual(parse_md.parse_h1(text), expected)