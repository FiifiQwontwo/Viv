from django.urls import path
from .views import listFaculty, detailsFaculty

app_name = 'faculty'

urlpatterns =[
      path('faculty/', listFaculty, name='facultyList_urls'),
      path('faculty/<slug:slug>/', detailsFaculty, name='faculty_details_urls')
]