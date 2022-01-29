from unicodedata import name
from django.shortcuts import render
import re


def library_view(request):
    return render(request, 'library.html')

def note_view(request, book_title, note_title):
    


    with open(f'notes/markdown/{book_title}/{note_title}.md', 'r') as f:
        text = f.read()
    return render(request, 'note.html', {'note_text': text})