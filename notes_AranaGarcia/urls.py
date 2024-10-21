from django.urls import path
from . import views

app_name = 'notes_AranaGarcia'

urlpatterns = [
    path('', views.note_list, name='note-list'),
    path('<int:pk>/', views.note_detail, name='note-detail'),
    path('new/', views.note_create, name='note-create'),
    path('<int:pk>/edit/', views.note_edit, name='note-edit'),
    path('<int:pk>/delete/', views.note_delete, name='note-delete'),
]
