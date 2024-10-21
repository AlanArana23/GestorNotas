from django.urls import path
from . import views

app_name = 'notes_AranaGarcia'

urlpatterns = [
    path('', views.note_list, name='note-list'),
    path('<int:notes_AranaGarcia>/', views.note_detail, name='note-detail'),
    path('new/', views.note_create, name='note-new'),
    path('<int:pk>/edit/', views.note_edit, name='note-edit'),
]
