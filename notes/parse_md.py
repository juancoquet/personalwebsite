import re


# md to html regex
h2 = r'^##\s(.+)$'
h3 = r'^###\s(.+)$'
h4 = r'^####\s(.+)$'
h5 = r'^#####\s(.+)$'
h6 = r'^######\s(.+)$'

def parse_h1(text):
    h1 = re.compile(r'^#\s(.+)$', re.MULTILINE)
    replaced = h1.sub(r'<h1>\1</h1>', text)
    return replaced