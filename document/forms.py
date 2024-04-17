from django import forms
from accounts.models import Student
from chapter.models import Chapter
from .models import Document


class DocumentUploader(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'content', 'chapter', 'student')

        chapter = forms.ModelChoiceField(label='chapter', queryset=Chapter.objects.all())

