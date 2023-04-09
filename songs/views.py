from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
# This is where we are going to define all the function that  the outside world can interact with.
#

@api_view(['GET'])   # inside the list is wshere we define what http method type are allow to be executed
def song_list (request):
   
    songs = Song.objects.all()

    serializer = SongSerializer(songs, many=True)
    

    return Response(serializer.data)