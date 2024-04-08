from django import forms
from .models import Document


class DocumentUploader(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content', 'chapter', 'student']

