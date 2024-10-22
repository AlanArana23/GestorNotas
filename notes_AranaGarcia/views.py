from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Note

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Note
from django.urls import reverse
# Lista de notas
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_AranaGarcia/note_list_AranaGarcia.html', {'notes': notes})

# Detalle de nota
# notes_AranaGarcia/views.py
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes_AranaGarcia/note_detail_AranaGarcia.html', {'note': note})

def note_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(user=request.user, title=title, content=content)
        return redirect('note_list_AranaGarcia')
    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html')

# Editar nota existente
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('note_detail', pk=pk)
    return render(request, 'notes_AranaGarcia/note_edit_AranaGarcia.html', {'note': note})

# Eliminar nota
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
