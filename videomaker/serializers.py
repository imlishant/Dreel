# serializers.py in yourapp

from rest_framework import serializers
from .models import UploadedHTML

class HTMLUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedHTML
        fields = ('html_file',)
