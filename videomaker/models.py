from django.db import models

# Create your models here.
class UploadedHTML(models.Model):
    html_file = models.FileField(upload_to='uploaded_html/')