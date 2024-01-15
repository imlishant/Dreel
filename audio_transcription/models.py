from django.db import models

# Create your models here.

class Transcription(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    video_file = models.FileField(upload_to='video/', null=True, blank=True)
    json_file = models.FileField(upload_to='json/', null=True, blank=True)
