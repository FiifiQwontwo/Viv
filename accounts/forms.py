from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student, LevelChoices, Lecturer, LecTitle
from faculty.models import Faculty
from course.models import Course


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    course = forms.ModelChoiceField(label='course', queryset=Course.objects.all())
    index_number = forms.CharField(label='Index Number', max_length=15)
    phone = forms.CharField(label='Phone Number', max_length=15)
    level = forms.ChoiceField(label='Level', choices=LevelChoices)
    # slug = forms.SlugField(label='Slug')

    # def clean_slug(self):
    #     slug = self.cleaned_data['slug']
    #     if not slug:
    #         slug = self.cleaned_data['index_number']
    #     return slug


class LecturerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    title = forms.ChoiceField(label='LecTitle')
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    staff_id = forms.CharField(label='Staff_Id', max_length=50)
    faculty = forms.ModelChoiceField(label='faculty', queryset=Faculty.objects.all())
    phone = forms.CharField(label='Phone Number', max_length=15)


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'index_number', 'level', 'course', 'phone')


class LecturerProfileForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('title', 'first_name', 'last_name', 'staff_id', 'phone', 'faculty')
