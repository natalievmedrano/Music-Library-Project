# Create your views here.
from django.shortcuts import get_object_or_404
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

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request,pk):
    song= get_object_or_404(Songs, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   