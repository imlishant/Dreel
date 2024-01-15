from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transcription
from .serializers import TranscriptionSerializer
import subprocess

class TranscriptionViewSet(viewsets.ModelViewSet):
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer

    def create(self, request, *args, **kwargs):
        audio_file = request.data.get('audio_file')

        # Run transcription code here
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', audio_file,
            '-vn',
            '-acodec', 'libmp3lame',
            '-ab', '192k',
            '-ar', '44100',
            '-y',
            'sample_aud.mp3'
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
        except subprocess.CalledProcessError as e:
            return Response({'error': str(e)}, status=400)

        # Continue with the remaining transcription code

        # Save transcription details
        instance = Transcription(audio_file=audio_file)
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
