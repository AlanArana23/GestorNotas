from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Note

# Lista de notas del usuario
def note_list(request):
    lista_notas = Note.objects.order_by('-creation_date')
    context = {
        "lista_notas": lista_notas,
    }
    return render(request, "notes_AranaGarcia/note_list_AranaGarcia.html", context)


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    context = {'note': note}
    return render(request, 'notes_AranaGarcia/note_detail_AranaGarcia.html', context)

# Crear una nueva nota
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            # Crear la nota
            Note.objects.create(user=request.user, title=title, content=content)
            return HttpResponseRedirect(reverse('notes_AranaGarcia:note-list'))
        else:
            # Mensaje de error si faltan campos
            return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html')
    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html')


# Editar una nota existente
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            # Guardar cambios de la nota
            note.title = title
            note.content = content
            note.save()
            return HttpResponseRedirect(reverse('notes_AranaGarcia:note-detail', args=(note.pk,)))
        else:
            # Mensaje de error si faltan campos
            return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html',
                          {'note': note, 'error_message': 'Todos los campos son obligatorios.'})

    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html', {'note': note})
