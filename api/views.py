from django.shortcuts import render
from .serializers import VideoElementSerializer, AudioFragmentSerializer
from .models import VideoElement, AudioFragment 
from rest_framework import viewsets

# Create your views here.

class VideoElementViewSet(viewsets.ModelViewSet):
    queryset = VideoElement.objects.all()
    serializer_class = VideoElementSerializer

class AudioFragmentViewSet(viewsets.ModelViewSet):
    queryset = AudioFragment.objects.all()
    serializer_class = AudioFragmentSerializer