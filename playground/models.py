from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=100)
    videos = models.FileField(upload_to='videos/')  # This field stores the uploaded videos
    uploaded_at = models.DateTimeField(auto_now_add=True)