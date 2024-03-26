from django.db import models
from chapter.models import Chapter
# Create your models here.

class Document(m
    title = models.CharField(max_length=100)
    content = models.FileUploadField()