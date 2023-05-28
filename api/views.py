from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VideoElementSerializer, AudioFragmentSerializer, AudioElementSerializer
from .models import VideoElement, AudioFragment, AudioElement
from rest_framework import viewsets


"""class VideoElementViewSet(viewsets.ModelViewSet):
    queryset = VideoElement.objects.all()
    serializer_class = VideoElementSerializer


class AudioFragmentViewSet(viewsets.ModelViewSet):
    queryset = AudioFragment.objects.all()
    serializer_class = AudioFragmentSerializer"""

@api_view(['GET'])
def audio_elements(request):
    if request.method == 'GET':
        audio_elements = AudioElement.objects.all()
        audio_fragments = AudioFragment.objects.all()
        audio_elements_serializer = AudioElementSerializer(audio_elements, many=True)
        return Response(audio_elements_serializer.data)

        
@api_view(['GET'])
def audio_fragments(request, fk):
    if request.method == 'GET':
        audio_fragments = AudioFragment.objects.filter(audio_element=fk)
        audio_fragments_serializer = AudioFragmentSerializer(audio_fragments, many=True)
        return Response(audio_fragments_serializer.data)

