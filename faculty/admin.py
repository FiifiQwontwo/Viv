from django.contrib import admin
from .models import Faculty
from course.models import Course
from accounts.models import Student, Lecturer, CustomUser

# Register your models here.

admin.site.site_header = "Lunch Lady"
admin.site.site_title = "Lunch Lady Admin"
admin.site.index_title = "Lunch Lady"


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['faculty_name']
    list_per_page = 20
    prepopulated_fields = {'slug': ('faculty_name',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['faculty', 'course_name']
    list_display = ['course_name', 'faculty']
    list_per_page = 20
    prepopulated_fields = {'slug': ('course_name',)}


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'index_number', 'level', 'course')
    list_filter = ('level', 'course')
    search_fields = ('first_name', 'last_name', 'index_number')
    ordering = ('last_name', 'first_name')
    fieldsets = ()
    # prepopulated_fields = {'slug': ('index_number',)}


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_name', 'first_name')
    list_filter = ('faculty',)
    search_fields = ('last_name', 'faculty__faculty_name')
    ordering = ('title',)
    fieldsets = ()
    # prepopulated_fields = {'slug': ('staff_id',)}


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email',  'last_login', 'date_joined')
    list_display_links = ('email',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    # Used so the other required fields such as groups is disabled
    filter_horizontal = ()
    list_filter = ()
    # Used to make password read only
    fieldsets = ()
