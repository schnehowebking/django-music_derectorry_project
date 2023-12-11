from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician
from album.models import Album
from .forms import MusicianForm

# Create your views here.

def musicians_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician/index.html', {'musicians': musicians})

def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = MusicianForm()
    return render(request, 'musician/addmusician.html', {'form': form})

def musician_detail(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    albums = Album.objects.filter(musician=musician)
    return render(request, 'musician/musicians_details.html', {'musician': musician, 'albums': albums})

def edit_musician(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_detail', pk=pk)
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musician/edit_musician.html', {'form': form, 'musician': musician})


def delete_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    albums = musician.album_set.all()
    albums.delete()
    musician.delete()

    return redirect('musicians_list')