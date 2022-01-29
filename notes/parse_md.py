import re


def parse_h1(markdown):
    h1 = re.compile(r'^#\s(.+)$', re.MULTILINE)
    replaced = h1.sub(r'<h1>\1</h1>', markdown)
    return replaced

def parse_h2(markdown):
    h2 = re.compile(r'^##\s(.+)$', re.MULTILINE)
    replaced = h2.sub(r'<h2>\1</h2>', markdown)
    return replaced

def parse_h3(markdown):
    h3 = re.compile(r'^###\s(.+)$', re.MULTILINE)
    replaced = h3.sub(r'<h3>\1</h3>', markdown)
    return replaced