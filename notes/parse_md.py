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