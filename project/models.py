from django.db import models
from accounts.models import Student
from document.models import Document


# Create your models here.
class Project(models.Model):
    pro_title = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    documents = models.ForeignKey(Document, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
