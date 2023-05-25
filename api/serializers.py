from rest_framework import serializers
from .models import VideoElement, AudioFragment


class VideoElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoElement
        fields = '__all__'


class AudioFragmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFragment
        fields = '__all__'