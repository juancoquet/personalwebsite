from django.urls import path

from .views import library_view, note_view


urlpatterns = [
    path('<str:book_title>/<str:note_title>/', note_view, name='note'),
    path('', library_view, name='library'),
]