from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class VideoElement(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200, null=True)


class AudioFragment(models.Model):

    choices = (
        ('vo', 'voice over'),
        ('bg_music', 'background music'),
        ('video_music', 'video music'),
    )

    id = models.AutoField(primary_key=True)
    audio_type = models.CharField(max_length=30, choices=choices)
    volume = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    video_element = models.ForeignKey(VideoElement, on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.IntegerField(null=True)
    end_time = models.IntegerField(null=True)
