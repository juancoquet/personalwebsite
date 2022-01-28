from unicodedata import name
from django.shortcuts import render
import re


def library_view(request):
    return render(request, 'library.html')

def note_view(request, book_title, note_title):
    


    with open(f'notes/markdown/{book_title}/{note_title}.md', 'r') as f:
        text = f.read()

        # first match paired ``` code block that spans multiple lines
        # code_re = re.compile(r'(```)(.+?)(```)')
        # replaced_text = code_re.sub(r'<pre><code>\2</code></pre>', text)
        test_re = re.compile(r'Note Type')
        replaced_text = test_re.sub(r'TEST', text)  # works

        
        # lines = f.readlines()
        # for line in lines:
        #     if re.match(h1, line):
        #         match = re.search(h1, line)
            
        # print(match)
        # text = ''.join(lines)
    return render(request, 'note.html', {'note_text': replaced_text})