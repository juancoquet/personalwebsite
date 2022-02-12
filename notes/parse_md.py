from django.urls import reverse
import os
import re


def parse_markdown(markdown):
    markdown = replace_special_characters(markdown)
    markdown = parse_wiki_links(markdown)
    markdown = parse_h1(markdown)
    markdown = parse_h2(markdown)
    markdown = parse_h3(markdown)
    markdown = parse_h4(markdown)
    markdown = parse_h5(markdown)
    markdown = parse_h6(markdown)
    markdown = parse_p(markdown)
    markdown = parse_bold(markdown)
    markdown = parse_italic(markdown)
    markdown = parse_hr(markdown)
    markdown = parse_ul(markdown)
    markdown = parse_ol(markdown)
    markdown = parse_inline_code(markdown)
    markdown = parse_code_block(markdown) # keep this at the end
    return markdown

def replace_special_characters(markdown):
    amp = re.compile(r'&')
    replaced = amp.sub(r'&amp;', markdown)
    gt = re.compile(r'>')
    replaced = gt.sub(r'&gt;', replaced)
    lt = re.compile(r'<')
    replaced = lt.sub(r'&lt;', replaced)
    return replaced

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
            line = re_pattern.sub(r'<{}>\1</{}>'.format(tag, tag), line)
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

def parse_ul(markdown):
    # supports one level of nesting
    ul = re.compile(r'(?P<main>^\t*-\s.+$(\n\t*-\s.+$)*)', re.MULTILINE)
    replaced = ul.sub(r'<ul>\n\g<main>\n</ul>', markdown)
    nested = re.compile(r'(?P<main>^\t+-\s.+$(\n\t+-\s.+$)*)', re.MULTILINE)
    replaced = nested.sub(r'<ul>\n\g<main>\n</ul>', replaced)
    li = re.compile(r'(^(?:\t*-\s)(.+)$)', re.MULTILINE)
    replaced = li.sub(r'<li>\2</li>', replaced)
    return replaced

def parse_ol(markdown):
    ol = re.compile(r'(?P<main>^\d+\.\s.+$(\n\d+\.\s.+$)*)', re.MULTILINE)
    replaced = ol.sub(r'<ol>\n\g<main>\n</ol>', markdown)
    nested = re.compile(r'(?P<main>^\t+\d+\.\s.+$(\n\t+\d+\.\s.+$)*)', re.MULTILINE)
    replaced = nested.sub(r'<ol>\n\g<main>\n</ol>', replaced)
    li = re.compile(r'(^(?:\d+\.\s)(.+)$)', re.MULTILINE)
    replaced = li.sub(r'<li>\2</li>', replaced)
    return replaced

def parse_wiki_links(markdown):
    wiki_link = re.compile(r'\[\[(?P<note_title>.+?)(\|(?P<alias>.+?))?\]\]')
    linked_notes = wiki_link.finditer(markdown)
    for link in linked_notes:
        title = link.group('note_title')
        alias = link.group('alias')
        source = locate_note_source(title)
        if source:
            url = reverse('note', kwargs={'note_title': title, 'book_title': source})
        else:
            url = reverse('note_not_found', kwargs={'note_title': title})
        if alias:
            html = f'<a href="{url}">{alias}</a>'
        else:
            html = f"""<a href="{url}">{title}</a>"""
        markdown = wiki_link.sub(html, markdown, 1)

    return markdown                

def locate_note_source(note_title):
    os.chdir('notes/markdown')
    note_title += '.md'
    source = None
    for curr_path, dirs, files in os.walk('.'):
        for file in files:
            if file == note_title:
                source = curr_path.split('/')[1]
                break
    os.chdir('../..')
    return source


if __name__ == '__main__':
    md = 'note that links to [[Functional tests]] and then to [[TDD workflow]]'
    print(parse_wiki_links(md))