from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Note

# Lista de notas
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-creation_date')
    context = {'notes': notes}
    return render(request, 'notes_AranaGarcia/note_list_AranaGarcia.html', context)

# Detalle de una nota
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    context = {'note': note}
    return render(request, 'notes_AranaGarcia/note_detail_AranaGarcia.html', context)

# Crear una nueva nota
def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if title and content:
            Note.objects.create(user=request.user, title=title, content=content)
            return HttpResponseRedirect(reverse('notas_AranaGarcia:note-list'))
        else:
            return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html', {'error_message': 'Todos los campos son obligatorios.'})
    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html')

# Editar una nota
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        if note.title and note.content:
            note.save()
            return HttpResponseRedirect(reverse('notas_AranaGarcia:note-detail', args=(note.pk,)))
        else:
            return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html', {'note': note, 'error_message': 'Todos los campos son obligatorios.'})
    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html', {'note': note})

# Eliminar una nota
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return HttpResponseRedirect(reverse('notas_AranaGarcia:note-list'))
    return render(request, 'notes_AranaGarcia/note_confirm_delete_AranaGarcia.html', {'note': note})
