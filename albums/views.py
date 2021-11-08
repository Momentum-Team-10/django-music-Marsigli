from django.shortcuts import render
# importing http library
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from albums.models import Album


# This function prints hello world ...etc when you are at the albums index level
def index(request):
    ## Get an array of all of the rows of values for your Album objects in the db
    albums = Album.objects.values()
    ## Convert that to a list (because we'll want to run a sort on it)
    albums = list(albums)
    ## Perform a custom sort function 
    ## Used this resource to sort a list of dictionary entries by a specific key:
    ## https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
    albums = sorted(albums, key=lambda d: d['title'])
    return render(request, 'base.html', {'albums':albums})

def new_album(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        q = Album(title=request.POST['title'], artist=request.POST['artist'], created_at=timezone.now())
        q.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_album.html')
    
def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'POST':
        album.delete();
        return HttpResponseRedirect('/')
    else:
        return render(request, 'delete_album.html', {'album':album})

def edit_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'POST':
        album.title = request.POST['title']
        album.artist = request.POST['artist']
        album.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'edit_album.html', {'album':album})

