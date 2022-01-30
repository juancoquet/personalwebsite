import re

from django.test import tag


def parse_markdown(markdown):
    markdown = parse_h1(markdown)
    markdown = parse_h2(markdown)
    markdown = parse_h3(markdown)
    markdown = parse_h4(markdown)
    markdown = parse_h5(markdown)
    markdown = parse_h6(markdown)
    markdown = parse_p(markdown)
    markdown = parse_inline_code(markdown)
    markdown = parse_bold(markdown)
    markdown = parse_italic(markdown)
    markdown = parse_hr(markdown)
    markdown = parse_ul(markdown)
    markdown = parse_code_block(markdown) # keep this at the end
    return markdown

def parse_code_block(markdown):
    code_block = re.compile(r'^```.*?$(.+?)^```$', re.MULTILINE | re.DOTALL)
    replaced = code_block.sub(r'<pre><code>\1</code></pre>', markdown)
    return replaced

def parse_outside_code_block(markdown, re_pattern, tag):
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block:
            line = re_pattern.sub(r'<%s>\1</%s>' % (tag, tag), line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_h1(markdown):
    h1 = re.compile(r'^#\s(.+)$', re.MULTILINE)
    tag = 'h1'
    return parse_outside_code_block(markdown, h1, tag)

def parse_h2(markdown):
    h2 = re.compile(r'^##\s(.+)$', re.MULTILINE)
    tag = 'h2'
    return parse_outside_code_block(markdown, h2, tag)

def parse_h3(markdown):
    h3 = re.compile(r'^###\s(.+)$', re.MULTILINE)
    tag = 'h3'
    return parse_outside_code_block(markdown, h3, tag)

def parse_h4(markdown):
    h4 = re.compile(r'^####\s(.+)$', re.MULTILINE)
    tag = 'h4'
    return parse_outside_code_block(markdown, h4, tag)

def parse_h5(markdown):
    h5 = re.compile(r'^#####\s(.+)$', re.MULTILINE)
    tag = 'h5'
    return parse_outside_code_block(markdown, h5, tag)

def parse_h6(markdown):
    h6 = re.compile(r'^######\s(.+)$', re.MULTILINE)
    tag = 'h6'
    return parse_outside_code_block(markdown, h6, tag)

def parse_p(markdown):
    p = re.compile(r'^((?!```|#{1,6}\s|>\s|-\s|\*\s|\d+.\s|^---$).*)$', re.MULTILINE)
    tag = 'p'
    return parse_outside_code_block(markdown, p, tag)

def parse_inline_code(markdown):
    inline_code = re.compile(r'`((?!`).+?)`')
    tag = 'code'
    return parse_outside_code_block(markdown, inline_code, tag)

def parse_bold(markdown):
    bold = re.compile(r'\*\*(.+?)\*\*')
    tag = 'strong'
    return parse_outside_code_block(markdown, bold, tag)

def parse_italic(markdown):
    italic = re.compile(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)')
    tag = 'em'
    return parse_outside_code_block(markdown, italic, tag)

def parse_hr(markdown):
    hr = re.compile(r'^---$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block and line.startswith('---'):
            line = hr.sub(r'<hr>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

# def parse_ul(markdown):
#     # flattens any nested lists
#     ul = re.compile(r'(^-\s.+$(\n\t*-\s.+$)*)', re.MULTILINE)
#     replaced = ul.sub(r'<ul>\n\1\n</ul>', markdown)
#     li = re.compile(r'(^(?:\t*-\s)(.+)$)', re.MULTILINE)
#     replaced = li.sub(r'<li>\2</li>', replaced)
#     return replaced

def parse_ul(markdown):
    # supports one level of nesting
    ul = re.compile(r'(?P<main>^\t*-\s.+$(\n\t*-\s.+$)*)', re.MULTILINE)
    replaced = ul.sub(r'<ul>\n\g<main>\n</ul>', markdown)
    nested = re.compile(r'(?P<main>^\t+-\s.+$(\n\t+-\s.+$)*)', re.MULTILINE)
    replaced = nested.sub(r'<ul>\n\g<main>\n</ul>', replaced)
    li = re.compile(r'(^(?:\t*-\s)(.+)$)', re.MULTILINE)
    replaced = li.sub(r'<li>\2</li>', replaced)
    return replaced