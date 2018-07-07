#from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader    //template non shortcut method
from django.shortcuts import render , get_object_or_404     # template shorcut method
from .models import Album


def index(request):
    all_albums = Album.objects.all()
#    template = loader.get_template('music/index.html')     //template using,non shortcut method
    return render(request, 'music/index.html', {'all_albums': all_albums})
#    html =''
#    for album in all_albums:
#        url = '/music/' + str(album.id) + '/'
#        html += '<a href="' + url + '">' + album.album_title +'</a><br>'
#    return HttpResponse(template.render(context,request))       #inside () write html,if not using templates
# Create your views here.


def detail(request, album_id):
#    return HttpResponse("<h2>Details for the album id: " + str(album_id) + "</h2>" )
#    album = Album.objects.get(pk=album_id)         instead of this,do the below one
    album = get_object_or_404(Album, pk=album_id)    # A shortcut to try-except
#    try:
#        album = Album.objects.get(pk=album_id)
#    except Album.DoesNotExist:
#        raise Http404("Album does not exist!")
    return render(request, 'music/detail.html', {'album': album})
