from unittest import TestCase
from unittest import skip

from .. import parse_md


class ParserTest(TestCase):

    def test_parse_h1(self):
        text = '# Title being tested'
        result = parse_md.parse_h1(text)
        expected = '<h1>Title being tested</h1>'
        self.assertEqual(result, expected)

    def test_parse_h1_on_multiple_lines(self):
        text = 'preceding text\n# Title being tested\nsome more text'
        result = parse_md.parse_h1(text)
        expected = 'preceding text\n<h1>Title being tested</h1>\nsome more text'
        self.assertEqual(result, expected)

    def test_unintended_hash_symbol_doesnt_parse_to_h1(self):
        text = 'the following # should not match'
        result = parse_md.parse_h1(text)
        expected = 'the following # should not match'
        self.assertEqual(result, expected)

    def test_multiple_h1_parses(self):
        text = '# Title being tested\nsome random text\n# Title being tested2'
        result = parse_md.parse_h1(text)
        expected = '<h1>Title being tested</h1>\nsome random text\n<h1>Title being tested2</h1>'
        self.assertEqual(result, expected)