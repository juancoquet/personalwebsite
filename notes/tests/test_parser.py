from django.urls import reverse
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

    def test_parse_inline_code(self):
        text = 'this is a paragraph with `inline code`'
        result = parse_md.parse_inline_code(text)
        expected = 'this is a paragraph with <code>inline code</code>'
        self.assertEqual(result, expected)

    def test_parse_inline_code_does_not_parse_inside_code_block(self):
        text = '```\n`this should not parse`\n```'
        result = parse_md.parse_inline_code(text)
        expected = '```\n`this should not parse`\n```'
        self.assertEqual(result, expected)

    def test_parse_bold(self):
        text = 'this is a paragraph with **bold text**'
        result = parse_md.parse_bold(text)
        expected = 'this is a paragraph with <strong>bold text</strong>'
        self.assertEqual(result, expected)

    def test_parse_bold_does_not_parse_inside_code_block(self):
        text = '```\n**this should not parse**\n```'
        result = parse_md.parse_bold(text)
        expected = '```\n**this should not parse**\n```'
        self.assertEqual(result, expected)
    
    def test_parse_italic(self):
        text = 'this is a paragraph with *italic text*'
        result = parse_md.parse_italic(text)
        expected = 'this is a paragraph with <em>italic text</em>'
        self.assertEqual(result, expected)

    def test_parse_italic_does_not_parse_inside_code_block(self):
        text = '```\n*this should not parse*\n```'
        result = parse_md.parse_italic(text)
        expected = '```\n*this should not parse*\n```'
        self.assertEqual(result, expected)

    def test_parse_italic_does_not_parse_bold(self):
        text = 'this is a paragraph with **bold text**'
        result = parse_md.parse_italic(text)
        expected = 'this is a paragraph with **bold text**'
        self.assertEqual(result, expected)

    def test_parse_hr(self):
        text = 'this is a paragraph\n\n---\nmore text'
        result = parse_md.parse_hr(text)
        expected = 'this is a paragraph\n\n<hr>\nmore text'
        self.assertEqual(result, expected)

    def test_parse_hr_does_not_parse_inside_code_block(self):
        text = '```\n---\n```'
        result = parse_md.parse_hr(text)
        expected = '```\n---\n```'
        self.assertEqual(result, expected)

    def test_hr_does_not_parse_mid_paragraph(self):
        text = 'this --- should not parse'
        result = parse_md.parse_hr(text)
        expected = 'this --- should not parse'
        self.assertEqual(result, expected)

    def test_parse_ul(self):
        text = 'this is a paragraph\n- item 1\n- item 2\n- item 3\nmore text'
        result = parse_md.parse_ul(text)
        expected = 'this is a paragraph\n<ul>\n<li>item 1</li>\n<li>item 2</li>\n<li>item 3</li>\n'\
            '</ul>\nmore text'
        self.assertEqual(result, expected)

    def test_parse_multiple_ul(self):
        text = 'this is a paragraph\n- item 1\n- item 2\nmore text before another list\n- item 3\n- item 4\n'\
            'more text after another list'
        result = parse_md.parse_ul(text)
        expected = 'this is a paragraph\n<ul>\n<li>item 1</li>\n<li>item 2</li>\n</ul>\n'\
            'more text before another list\n<ul>\n<li>item 3</li>\n<li>item 4</li>\n</ul>\n'\
            'more text after another list'
        self.assertEqual(result, expected)

    def test_parse_sub_ul(self):
        text = '- item 1\n\t- sub item 1\n\t- sub item 2\n- item 2\n\t- sub item 3'
        result = parse_md.parse_ul(text)
        expected = '<ul>\n<li>item 1</li>\n<ul>\n<li>sub item 1</li>\n<li>sub item 2</li>\n</ul>\n'\
            '<li>item 2</li>\n<ul>\n<li>sub item 3</li>\n</ul>\n</ul>'
        self.assertEqual(result, expected)

    def test_parse_ol(self):
        text = 'this is a paragraph\n1. item 1\n2. item 2\n3. item 3\nmore text'
        result = parse_md.parse_ol(text)
        expected = 'this is a paragraph\n<ol>\n<li>item 1</li>\n<li>item 2</li>\n<li>item 3</li>\n'\
            '</ol>\nmore text'
        self.assertEqual(result, expected)
    
    def test_parse_multiple_ol(self):
        text = 'this is a paragraph\n1. item 1\n2. item 2\nmore text before another list\n1. item 3\n'\
            '2. item 4\nmore text after another list'
        result = parse_md.parse_ol(text)
        expected = 'this is a paragraph\n<ol>\n<li>item 1</li>\n<li>item 2</li>\n</ol>\n'\
            'more text before another list\n<ol>\n<li>item 3</li>\n<li>item 4</li>\n</ol>\n'\
            'more text after another list'
        self.assertEqual(result, expected)

    def test_replace_html_characters(self):
        text = 'this <code>should change to encoded symbols</code>'
        result = parse_md.replace_special_characters(text)
        expected = 'this &lt;code&gt;should change to encoded symbols&lt;/code&gt;'
        self.assertEqual(result, expected)

    def test_parse_wiki_link(self):
        text = 'this links to the [[Functional tests]] note'
        result = parse_md.parse_wiki_links(text).replace('%20', ' ')
        expected = 'this links to the <a href="/notes/Test Driven Development with Python/'\
            'Functional tests/">Functional tests</a> note'
        self.assertEqual(result, expected)

    def test_parse_multiple_wiki_links(self):
        text = '[[Functional tests]] [[TDD workflow]]'
        result = parse_md.parse_wiki_links(text).replace('%20', ' ')
        expected = '<a href="/notes/Test Driven Development with Python/Functional tests/">Functional tests</a> '\
            '<a href="/notes/Test Driven Development with Python/TDD workflow/">TDD workflow</a>'
        self.assertEqual(result, expected)

    def test_link_to_note_not_found_links_to_note_not_found_page(self):
        text = "this note [[doesn't exist]]"
        result = parse_md.parse_wiki_links(text)
        url = reverse('note_not_found', kwargs={'note_title': 'doesn\'t exist'})
        expected = f"""this note <a href="{url}">doesn't exist</a>"""
        self.assertEqual(result, expected)

    def test_parse_wiki_link_alias(self):
        text = 'this note has an alias [[TDD workflow|alias name]]'
        result = parse_md.parse_wiki_links(text)
        url = reverse('note', kwargs={'note_title': 'TDD workflow',
        'source_title': 'Test Driven Development with Python'})
        expected = f'this note has an alias <a href="{url}">alias name</a>'
        self.assertEqual(result, expected)

    def test_parse_wiki_links_case_insensitive(self):
        text = "[[tdd workflow]]"
        result = parse_md.parse_wiki_links(text)
        expected_url = reverse('note', kwargs={'note_title': 'TDD workflow',
        'source_title': 'Test Driven Development with Python'})
        expected = f'<a href="{expected_url}">tdd workflow</a>'
        self.assertEqual(result, expected)

    def test_parse_image_embed(self):
        text = 'some text\n![alt text](http://www.example.com/path/to/img.jpg)\nmore text'
        result = parse_md.parse_image(text)
        expected = 'some text\n<img src="http://www.example.com/path/to/img.jpg" alt="alt text">\nmore text'
        self.assertEqual(result, expected)

    def test_parse_multiple_image_embed(self):
        text = 'some text\n![alt text](http://www.example.com/path/to/img.jpg)\nmore text\n![alt text 2](http://www.example2.com/path/to/img2.jpg)'
        result = parse_md.parse_image(text)
        expected = 'some text\n<img src="http://www.example.com/path/to/img.jpg" alt="alt text">\nmore text\n'\
            '<img src="http://www.example2.com/path/to/img2.jpg" alt="alt text 2">'
        self.assertEqual(result, expected)

    def test_parse_image_from_file_path(self):
        text = 'some text\n![tdd workflow](tdd-workflow.png)\nmore text'
        result = parse_md.parse_image(text)
        expected = 'some text\n<img src="/static/img/notes/tdd-workflow.png" '\
            'alt="tdd workflow">\nmore text'
        self.assertEqual(result, expected)

    @skip
    def test_parse_image_from_static_folder(self):
        self.fail()

    @skip
    def test_parse_image_file_embed(self):
        text = 'some text\n![[tdd-workflow.png]]'
        self.fail('not implemented')

    def test_remove_note_type(self):
        text = 'Note type: #litnote\n\n---\nnote body'
        result = parse_md.remove_note_type(text)
        expected = '\n\n---\nnote body'
        self.assertEqual(result, expected)

    def test_remove_permanotes(self):
        text = 'some text\n### See also\n- [[TDD workflow]]\n\n'\
        '### permanotes\n- [[another note]]'
        result = parse_md.remove_permanotes(text)
        expected = 'some text\n### See also\n- [[TDD workflow]]'
        self.assertEqual(result, expected)

    def test_remove_frontmatter(self):
        text = '---\naliases: []\nDate: 2022-02-09\n---\n# note title\ntext'
        result = parse_md.remove_frontmatter(text)
        expected = '# note title\ntext'
        self.assertEqual(result, expected)

    def test_remove_frontmatter_does_not_remove_note_body(self):
        text = 'note type: #litnote\n---\n# heading\ntext\n\n---\n# see also\n- [[another note]]'
        result = parse_md.remove_frontmatter(text)
        expected = text
        self.assertEqual(result, expected)

    def test_parse_inline_tex(self):
        text = 'some text that has inline tex $a+b=2^c$'
        result = parse_md.parse_inline_tex(text)
        expected = 'some text that has inline tex \(a+b=2^c\)'
        self.assertEqual(result, expected)

    def test_parse_inline_tex_does_not_parse_tex_block(self):
        text = 'should not parse tex block\n\n$$a+b=2^c$$'
        result = parse_md.parse_inline_tex(text)
        expected = text
        self.assertEqual(result, expected)

    def test_remove_br(self):
        text = 'some text\n\n<br>\nmore text'
        result = parse_md.remove_br(text)
        expected = 'some text\n\n\nmore text'
        self.assertEqual(result, expected)