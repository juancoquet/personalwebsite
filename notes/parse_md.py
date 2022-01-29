import re


def parse_markdown(markdown):
    markdown = parse_h1(markdown)
    markdown = parse_h2(markdown)
    markdown = parse_h3(markdown)
    markdown = parse_h4(markdown)
    markdown = parse_h5(markdown)
    markdown = parse_h6(markdown)
    markdown = parse_p(markdown)
    markdown = parse_inline_code(markdown)
    markdown = parse_hr(markdown)
    markdown = parse_code_block(markdown) # keep this at the end
    return markdown

def parse_code_block(markdown):
    code_block = re.compile(r'^```.*?$(.+?)^```$', re.MULTILINE | re.DOTALL)
    replaced = code_block.sub(r'<pre><code>\1</code></pre>', markdown)
    return replaced

def parse_h1(markdown):
    h1 = re.compile(r'^#\s(.+)$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block and line.startswith('#'):
            line = h1.sub(r'<h1>\1</h1>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_h2(markdown):
    h2 = re.compile(r'^##\s(.+)$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block and line.startswith('##'):
            line = h2.sub(r'<h2>\1</h2>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_h3(markdown):
    h3 = re.compile(r'^###\s(.+)$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block and line.startswith('###'):
            line = h3.sub(r'<h3>\1</h3>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_h4(markdown):
    h4 = re.compile(r'^####\s(.+)$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block and line.startswith('####'):
            line = h4.sub(r'<h4>\1</h4>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_h5(markdown):
    h5 = re.compile(r'^#####\s(.+)$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block and line.startswith('#####'):
            line = h5.sub(r'<h5>\1</h5>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_h6(markdown):
    h6 = re.compile(r'^######\s(.+)$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block and line.startswith('######'):
            line = h6.sub(r'<h6>\1</h6>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_p(markdown):
    p = re.compile(r'^((?!```|#{1,6}\s|>\s|-\s|\*\s|\d+.\s|^---$).*)$', re.MULTILINE)
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block:
            line = p.sub(r'<p>\1</p>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

def parse_inline_code(markdown):
    inline_code = re.compile(r'`((?!`).+?)`')
    lines = markdown.split('\n')
    code_block = False
    replaced = []
    for line in lines:
        if line.startswith('```'):
            code_block = not code_block
        if not code_block:
            line = inline_code.sub(r'<code>\1</code>', line)
        replaced.append(line)
    replaced = '\n'.join(replaced)
    return replaced

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