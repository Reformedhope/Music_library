from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song
# This is where we are going to define all the function that  the outside world can interact with.
#

@api_view(['GET', 'POST'])   # inside the list is wshere we define what http method type are allow to be executed
def song_list (request):

    if request.method =='GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE' ])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
 

    
       