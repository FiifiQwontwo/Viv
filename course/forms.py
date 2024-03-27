from .models import Course
from django import forms
from faculty.models import Faculty


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            'course_name', 'faculty'
        )

    faculty = forms.ModelChoiceField(label='faculty', queryset=Faculty.objects.all())
    course_name = forms.CharField(label='course name', max_length=50)


