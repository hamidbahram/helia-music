from django.shortcuts import render
from django.views import generic
from . import models

def home(request):
    # import pdb; pdb.set_trace()
    ctx = {}
    ctx['album'] = album = models.Album.objects.first()
    ctx['tracks'] = tracks = models.Track.objects.filter(album=album)
    ctx['tracks_count'] = len(tracks)
    return render(request,'app_music/home.html', ctx)
