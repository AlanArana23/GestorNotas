from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Note

# Lista de notas
@login_required
def note_list(request):
    # Mostrar las notas del usuario autenticado
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes_AranaGarcia/note_list_AranaGarcia.html', {'notes': notes})

# Detalle de nota
@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes_AranaGarcia/note_detail_AranaGarcia.html', {'note': note})

# Crear nota
@login_required
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(user=request.user, title=title, content=content)
        # Redirigir usando el app_name
        return redirect('notes_AranaGarcia:note_list')
    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html')

# Editar nota
@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            note.title = title
            note.content = content
            note.save()
            # Redirigir usando el app_name
            return redirect('notes_AranaGarcia:note_detail', pk=note.pk)
    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html', {'note': note})

# Eliminar nota
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    # Redirigir usando el app_name
    return redirect('notes_AranaGarcia:note_list')
