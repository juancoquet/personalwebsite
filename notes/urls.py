from django.urls import path

from .views import library_view, note_not_found_view, note_view, note_not_found_view


urlpatterns = [
    path('note-not-found/<str:note_title>/', note_not_found_view, name='note_not_found'),
    path('<str:book_title>/<str:note_title>/', note_view, name='note'),
    path('', library_view, name='library'),
]