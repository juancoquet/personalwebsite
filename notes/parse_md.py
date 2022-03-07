from django.templatetags.static import static
from django.urls import reverse
import os
import re


def parse_markdown(markdown):
    markdown = remove_frontmatter(markdown)
    markdown = remove_permanotes(markdown)
    markdown = remove_note_type(markdown)
    markdown = remove_br(markdown)
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
    markdown = parse_image(markdown)
    markdown = parse_inline_tex(markdown)
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
    wiki_link = re.compile(r'(?<!!)\[\[(?P<note_title>.+?)(\|(?P<alias>.+?))?\]\]')
    linked_notes = wiki_link.finditer(markdown)
    for link in linked_notes:
        title = link.group('note_title')
        alias = link.group('alias')
        source, file_name = locate_note_source(title)
        if source:
            url = reverse('note', kwargs={'note_title': file_name, 'source_title': source})
        else:
            url = reverse('note_not_found', kwargs={'note_title': title})
        if alias:
            html = f'<a href="{url}">{alias}</a>'
        else:
            html = f"""<a href="{url}">{title}</a>"""
        markdown = wiki_link.sub(html, markdown, 1)

    return markdown

def parse_inline_tex(markdown):
    tex = re.compile(r'(?<!\$)\$(?!\$)(?P<tex>.+?)(?<!\$)\$(?!\$)')
    replaced = tex.sub(r'\\(\g<tex>\\)', markdown)
    return replaced


def remove_permanotes(markdown):
    permanotes = re.compile(r'^#+\sPermanotes$', re.MULTILINE|re.IGNORECASE)
    markdown = permanotes.split(markdown)
    return markdown[0].strip()

def remove_frontmatter(markdown):
    front_matter = re.compile(r'^---\n(.+?)\n---\n', re.DOTALL)
    markdown = front_matter.sub('', markdown)
    return markdown

def remove_note_type(markdown):
    note_type = re.compile(r'^note type:\s#.+?$', re.MULTILINE|re.IGNORECASE)
    markdown = note_type.sub('', markdown)
    return markdown

def remove_br(markdown):
    br = re.compile(r'<br>')
    markdown = br.sub('', markdown)
    return markdown

def locate_note_source(note_title):
    os.chdir('notes/markdown')
    note_title += '.md'
    source = None
    file_name = None
    for curr_path, dirs, files in os.walk('.'):
        for file in files:
            if file.lower() == note_title.lower():
                source = curr_path.split('/')[1]
                file_name = file.replace('.md', '')
                break
    os.chdir('../..')
    return source, file_name

def parse_image(markdown):
    image = re.compile(r'\!\[(?P<alt>.+?)\]\((?P<url>.+?)\)')
    image_links = image.finditer(markdown)
    for link in image_links:
        alt = link.group('alt')
        url = link.group('url')
        if not url.startswith('http'):
            url = create_static_path(url)
        html = f"""<img src="{url}" alt="{alt}">"""
        markdown = image.sub(html, markdown, 1)
    image = re.compile(r'\!\[\[(?P<filename>.+?\..+?)\]\]')
    image_embeds = image.finditer(markdown)
    for embed in image_embeds:
        url = create_static_path(embed.group('filename'))
        html = f'<img src="{url}">'
        markdown = image.sub(html, markdown, 1)
    return markdown

def create_static_path(image_name):
    url = "/static/img/notes/" + image_name
    return url



if __name__ == '__main__':
    text = 'some text that has tex block\n$$a+b=2^c$$'
    print(parse_inline_tex(text))