from unittest import TestCase
from unittest import skip

from .. import parse_md


class MarkdownParseTest(TestCase):

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

    def test_parse_code_block(self):
        text = '```python\nprint("hello world")\n```'
        result = parse_md.parse_code_block(text)
        expected = '<pre><code>\nprint("hello world")\n</code></pre>'
        self.assertEqual(result, expected)

    def test_parse_code_block_with_multiple_lines(self):
        text = 'preceding text\n```python\nprint("hello world")\nmy_var = 123\n```\nmore text'
        result = parse_md.parse_code_block(text)
        expected = 'preceding text\n<pre><code>\nprint("hello world")\nmy_var = 123\n</code></pre>\nmore text'
        self.assertEqual(result, expected)

    def test_parse_multiple_code_blocks(self):
        text = '```python\nprint("hello world")\n```\nrandom text\n```python\nprint("hello world2")\n```'
        result = parse_md.parse_code_block(text)
        expected = '<pre><code>\nprint("hello world")\n</code></pre>\nrandom text\n<pre><code>\nprint("hello world2")\n</code></pre>'
        self.assertEqual(result, expected)

    def test_parse_p(self):
        text = 'this is a paragraph'
        result = parse_md.parse_p(text)
        expected = '<p>this is a paragraph</p>'
        self.assertEqual(result, expected)

    def test_parse_p_on_multiple_lines(self):
        text = 'this is a paragraph\nthis is another paragraph'
        result = parse_md.parse_p(text)
        expected = '<p>this is a paragraph</p>\n<p>this is another paragraph</p>'
        self.assertEqual(result, expected)

    def test_p_does_not_parse_inside_code_block(self):
        text = 'this should parse\n```\nthis should not parse\n```\nthis should also parse'
        result = parse_md.parse_p(text)
        expected = '<p>this should parse</p>\n```\nthis should not parse\n```\n<p>this should also parse</p>'
        self.assertEqual(result, expected)

    def test_p_does_not_parse_heading(self):
        text = 'this should parse\n# this should not parse\nthis should also parse'
        result = parse_md.parse_p(text)
        expected = '<p>this should parse</p>\n# this should not parse\n<p>this should also parse</p>'
        self.assertEqual(result, expected)

    def test_p_does_not_parse_quote(self):
        text = 'this should parse\n> this should not parse\nthis should also parse'
        result = parse_md.parse_p(text)
        expected = '<p>this should parse</p>\n> this should not parse\n<p>this should also parse</p>'
        self.assertEqual(result, expected)

    def test_p_does_not_parse_unordered_list(self):
        text = 'this should parse\n- this should not parse\nthis should also parse\n* this should not parse either'
        result = parse_md.parse_p(text)
        expected = '<p>this should parse</p>\n- this should not parse\n<p>this should also parse</p>\n* this should not parse either'
        self.assertEqual(result, expected)

    def test_p_does_not_parse_ordered_list(self):
        text = 'this should parse\n1. this should not parse\nthis should also parse\n12. this should not parse either'
        result = parse_md.parse_p(text)
        expected = '<p>this should parse</p>\n1. this should not parse\n<p>this should also parse</p>\n12. this should not parse either'
        self.assertEqual(result, expected)