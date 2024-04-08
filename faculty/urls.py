from django.urls import path
from .views import listFaculty

app_name = 'faculty'

urlpatterns =[
      path('faculty/', listFaculty, name='facultyList_urls')
]