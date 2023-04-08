from rest_framework.decorators import api_view
from rest_framework.response import Response
# This is where we are going to define all the function that  the outside world can interact with.
#

@api_view(['GET'])   # inside the list is wshere we define what http method type are allow to be executed
def song_list (request):
    
    return Response('ok')