import re


def parse_h1(markdown):
    h1 = re.compile(r'^#\s(.+)$', re.MULTILINE)
    replaced = h1.sub(r'<h1>\1</h1>', markdown)
    return replaced