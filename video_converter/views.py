from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action 
import subprocess

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @action(detail=True, methods=['post'])
    def convert_video(self, request, pk=None):
        video = self.get_object()
        input_file = video.file.path
        mp4_output = f'media/uploads/{video.title}.mp4'
        mp3_output = f'media/uploads/{video.title}.mp3'
        subtitle_output = f'media/uploads/{video.title}.srt'

        # Convert to MP4
        
        # Convert any video format to .mp4 format 
        # ffmpeg -i input_video.xxx -c:v libx264 -c:a aac -strict experimental -b:a 192k output_video.mp4

        # Remove/Trim silence 
        # ffmpeg -i input_video.mp4 -af silenceremove=1:0:-50dB output_video_trimmed.mp4

        subprocess.run(['ffmpeg', '-i', input_file, mp4_output])

        # Convert to MP3
        subprocess.run(['ffmpeg', '-i', input_file, mp3_output])

        # Generate subtitle
        subprocess.run(['ffmpeg', '-i', input_file, subtitle_output])

        return Response({'message': 'Conversion completed'})
