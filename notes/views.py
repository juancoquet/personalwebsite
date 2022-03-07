from django.shortcuts import render
from django.utils.safestring import mark_safe


from .parse_md import parse_markdown


def notes_library_view(request):
    return render(request, 'library.html')

def note_view(request, book_title, note_title):
    with open(f'notes/markdown/{book_title}/{note_title}.md', 'r') as f:
        markdown = f.read()
    html = mark_safe(parse_markdown(markdown))
    return render(request, 'note.html', {'note_html': html})

def note_not_found_view(request, note_title):
    return render(request, 'note_not_found.html', {'note_title': note_title})