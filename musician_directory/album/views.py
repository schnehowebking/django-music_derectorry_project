from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.


def add_album(request):
    
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('musicians_list')
    else:
        form = AlbumForm()

    return render(request, 'album/add_album.html', {'form': form})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'album/album_details.html', {'album': album})


def edit_album(request,album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', album_id=album_id)
    else:
        form = AlbumForm(instance=album)

    return render(request, 'album/edit_album.html', {'form': form, 'album': album})


def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect('musicians_list')