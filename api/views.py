from django.shortcuts import render
from .serializers import VideoElementSerializer, AudioFragmentSerializer
from .models import VideoElement, AudioFragment 
from rest_framework import viewsets


"""this is the viewset for the video element model"""
class VideoElementViewSet(viewsets.ModelViewSet):
    queryset = VideoElement.objects.all()
    serializer_class = VideoElementSerializer

"""this is the viewset for the audio fragment model"""
class AudioFragmentViewSet(viewsets.ModelViewSet):
    queryset = AudioFragment.objects.all()
    serializer_class = AudioFragmentSerializer