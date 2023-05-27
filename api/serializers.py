from rest_framework import serializers
from .models import VideoElement, AudioFragment

"""this is the serializer for the video element model, it serializes all the fields in the model as JSON"""
class VideoElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoElement
        fields = '__all__'

"""this is the serializer for the audio fragment model, it serializes all the fields in the model as JSON"""
class AudioFragmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFragment
        fields = '__all__'