import re


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