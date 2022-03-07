from django.urls import path

from .views import notes_library_view, note_not_found_view, note_view, note_not_found_view


urlpatterns = [
    path('', notes_library_view, name='library'),
    path('note-not-found/<str:note_title>/', note_not_found_view, name='note_not_found'),
    path('<str:source_title>/<str:note_title>/', note_view, name='note'),
]