from django.urls import path
from . import views

app_name = 'notes_AranaGarcia'

urlpatterns = [
    # Lista de notas: ''
    path('', views.note_list, name='note_list'),

    # Detalle de nota: '<int:pk>/'
    path('<int:pk>/', views.note_detail, name='note_detail'),

    # Creación de nota: 'new/'
    path('new/', views.note_create, name='note_create'),

    # Edición de nota: '<int:pk>/edit/'
    path('<int:pk>/edit/', views.note_edit, name='note_edit'),

    path('<int:pk>/delete/', views.note_delete, name='note_delete'),

]
