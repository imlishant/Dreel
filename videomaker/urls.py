# urls.py in yourapp

from django.urls import path
from .views import HTMLUploadView
from .views import merge_videos


urlpatterns = [
    path('upload/', HTMLUploadView.as_view(), name='html-upload'),
    path('merge_videos/', merge_videos, name='merge_videos'),
]
