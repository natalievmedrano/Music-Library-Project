# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Songs


@api_view(['GET','POST'])
def songs_list(request):

    if request.method == 'GET':
        songs = Songs.objects.all()
        serializer= SongSerializer(songs , many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def song_detail(request,pk):
 try:
    song = Songs.objects.get(pk=pk)
    serializer = SongSerializer(song)
    return Response(serializer.data)
 except Songs.DoesNotExist:
    return Response(status= status.HTTP_404_NOT_FOUND)
   