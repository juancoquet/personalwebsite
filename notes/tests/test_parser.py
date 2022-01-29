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

    def test_multiple_h1_parses(self):
        text = '# Title being tested\nsome random text\n# Title being tested2'
        result = parse_md.parse_h1(text)
        expected = '<h1>Title being tested</h1>\nsome random text\n<h1>Title being tested2</h1>'
        self.assertEqual(result, expected)

    def test_unintended_hash_symbol_does_not_parse_to_h1(self):
        text = 'the following # should not match'
        result = parse_md.parse_h1(text)
        expected = 'the following # should not match'
        self.assertEqual(result, expected)

    def test_h1_does_not_parse_inside_code_block(self):
        text = '```\n# python comment\nmy_var = "hello world"\n```'
        result = parse_md.parse_h1(text)
        expected = '```\n# python comment\nmy_var = "hello world"\n```'
        self.assertEqual(result, expected)

    def test_h1_does_not_parse_inside_code_block_with_multiple_lines(self):
        text = '```\n# python comment\nmy_var = "hello world"\n# python comment2\n```'
        result = parse_md.parse_h1(text)
        expected = '```\n# python comment\nmy_var = "hello world"\n# python comment2\n```'
        self.assertEqual(result, expected)

    def test_parse_h2(self):
        text = '## Title being tested'
        result = parse_md.parse_h2(text)
        expected = '<h2>Title being tested</h2>'
        self.assertEqual(result, expected)

    def test_parse_h2_on_multiple_lines(self):
        text = 'preceding text\n## Title being tested\nsome more text'
        result = parse_md.parse_h2(text)
        expected = 'preceding text\n<h2>Title being tested</h2>\nsome more text'
        self.assertEqual(result, expected)

    def test_multiple_h2_parses(self):
        text = '## Title being tested\nsome random text\n## Title being tested2'
        result = parse_md.parse_h2(text)
        expected = '<h2>Title being tested</h2>\nsome random text\n<h2>Title being tested2</h2>'
        self.assertEqual(result, expected)

    def test_unintended_hash_symbol_does_not_parse_to_h2(self):
        text = 'the following ## should not match'
        result = parse_md.parse_h2(text)
        expected = 'the following ## should not match'
        self.assertEqual(result, expected)

    def test_h2_does_not_parse_inside_code_block(self):
        text = '```\n## python comment\nmy_var = "hello world"\n```'
        result = parse_md.parse_h2(text)
        expected = '```\n## python comment\nmy_var = "hello world"\n```'
        self.assertEqual(result, expected)

    def test_h2_does_not_parse_inside_code_block_with_multiple_lines(self):
        text = '```\n## python comment\nmy_var = "hello world"\n## python comment2\n```'
        result = parse_md.parse_h2(text)
        expected = '```\n## python comment\nmy_var = "hello world"\n## python comment2\n```'
        self.assertEqual(result, expected)

    def test_parse_h3(self):
        text = '### Title being tested'
        result = parse_md.parse_h3(text)
        expected = '<h3>Title being tested</h3>'
        self.assertEqual(result, expected)

    def test_parse_h3_on_multiple_lines(self):
        text = 'preceding text\n### Title being tested\nsome more text'
        result = parse_md.parse_h3(text)
        expected = 'preceding text\n<h3>Title being tested</h3>\nsome more text'
        self.assertEqual(result, expected)

    def test_multiple_h3_parses(self):
        text = '### Title being tested\nsome random text\n### Title being tested2'
        result = parse_md.parse_h3(text)
        expected = '<h3>Title being tested</h3>\nsome random text\n<h3>Title being tested2</h3>'
        self.assertEqual(result, expected)

    def test_unintended_hash_symbol_does_not_parse_to_h3(self):
        text = 'the following ### should not match'
        result = parse_md.parse_h3(text)
        expected = 'the following ### should not match'
        self.assertEqual(result, expected)

    def test_h3_does_not_parse_inside_code_block(self):
        text = '```\n### python comment\nmy_var = "hello world"\n```'
        result = parse_md.parse_h3(text)
        expected = '```\n### python comment\nmy_var = "hello world"\n```'
        self.assertEqual(result, expected)

    def test_h3_does_not_parse_inside_code_block_with_multiple_lines(self):
        text = '```\n### python comment\nmy_var = "hello world"\n### python comment2\n```'
        result = parse_md.parse_h3(text)
        expected = '```\n### python comment\nmy_var = "hello world"\n### python comment2\n```'
        self.assertEqual(result, expected)

    def test_parse_h4(self):
        text = '#### Title being tested'
        result = parse_md.parse_h4(text)
        expected = '<h4>Title being tested</h4>'
        self.assertEqual(result, expected)

    def test_parse_h4_on_multiple_lines(self):
        text = 'preceding text\n#### Title being tested\nsome more text'
        result = parse_md.parse_h4(text)
        expected = 'preceding text\n<h4>Title being tested</h4>\nsome more text'
        self.assertEqual(result, expected)

    def test_multiple_h4_parses(self):
        text = '#### Title being tested\nsome random text\n#### Title being tested2'
        result = parse_md.parse_h4(text)
        expected = '<h4>Title being tested</h4>\nsome random text\n<h4>Title being tested2</h4>'
        self.assertEqual(result, expected)

    def test_unintended_hash_symbol_does_not_parse_to_h4(self):
        text = 'the following #### should not match'
        result = parse_md.parse_h4(text)
        expected = 'the following #### should not match'
        self.assertEqual(result, expected)

    def test_h4_does_not_parse_inside_code_block(self):
        text = '```\n#### python comment\nmy_var = "hello world"\n```'
        result = parse_md.parse_h4(text)
        expected = '```\n#### python comment\nmy_var = "hello world"\n```'
        self.assertEqual(result, expected)

    def test_h4_does_not_parse_inside_code_block_with_multiple_lines(self):
        text = '```\n#### python comment\nmy_var = "hello world"\n#### python comment2\n```'
        result = parse_md.parse_h4(text)
        expected = '```\n#### python comment\nmy_var = "hello world"\n#### python comment2\n```'
        self.assertEqual(result, expected)

    def test_parse_h5(self):
        text = '##### Title being tested'
        result = parse_md.parse_h5(text)
        expected = '<h5>Title being tested</h5>'
        self.assertEqual(result, expected)

    def test_parse_h5_on_multiple_lines(self):
        text = 'preceding text\n##### Title being tested\nsome more text'
        result = parse_md.parse_h5(text)
        expected = 'preceding text\n<h5>Title being tested</h5>\nsome more text'
        self.assertEqual(result, expected)

    def test_multiple_h5_parses(self):
        text = '##### Title being tested\nsome random text\n##### Title being tested2'
        result = parse_md.parse_h5(text)
        expected = '<h5>Title being tested</h5>\nsome random text\n<h5>Title being tested2</h5>'
        self.assertEqual(result, expected)

    def test_unintended_hash_symbol_does_not_parse_to_h5(self):
        text = 'the following ##### should not match'
        result = parse_md.parse_h5(text)
        expected = 'the following ##### should not match'
        self.assertEqual(result, expected)

    def test_h5_does_not_parse_inside_code_block(self):
        text = '```\n###### python comment\nmy_var = "hello world"\n```'
        result = parse_md.parse_h5(text)
        expected = '```\n###### python comment\nmy_var = "hello world"\n```'
        self.assertEqual(result, expected)

    def test_h5_does_not_parse_inside_code_block_with_multiple_lines(self):
        text = '```\n###### python comment\nmy_var = "hello world"\n###### python comment2\n```'
        result = parse_md.parse_h5(text)
        expected = '```\n###### python comment\nmy_var = "hello world"\n###### python comment2\n```'
        self.assertEqual(result, expected)

    def test_parse_h6(self):
        text = '###### Title being tested'
        result = parse_md.parse_h6(text)
        expected = '<h6>Title being tested</h6>'
        self.assertEqual(result, expected)

    def test_parse_h6_on_multiple_lines(self):
        text = 'preceding text\n###### Title being tested\nsome more text'
        result = parse_md.parse_h6(text)
        expected = 'preceding text\n<h6>Title being tested</h6>\nsome more text'
        self.assertEqual(result, expected)

    def test_multiple_h6_parses(self):
        text = '###### Title being tested\nsome random text\n###### Title being tested2'
        result = parse_md.parse_h6(text)
        expected = '<h6>Title being tested</h6>\nsome random text\n<h6>Title being tested2</h6>'
        self.assertEqual(result, expected)

    def test_unintended_hash_symbol_does_not_parse_to_h6(self):
        text = 'the following ###### should not match'
        result = parse_md.parse_h6(text)
        expected = 'the following ###### should not match'
        self.assertEqual(result, expected)

    def test_h6_does_not_parse_inside_code_block(self):
        text = '```\n####### python comment\nmy_var = "hello world"\n```'
        result = parse_md.parse_h6(text)
        expected = '```\n####### python comment\nmy_var = "hello world"\n```'
        self.assertEqual(result, expected)

    def test_h6_does_not_parse_inside_code_block_with_multiple_lines(self):
        text = '```\n####### python comment\nmy_var = "hello world"\n####### python comment2\n```'
        result = parse_md.parse_h6(text)
        expected = '```\n####### python comment\nmy_var = "hello world"\n####### python comment2\n```'
        self.assertEqual(result, expected)