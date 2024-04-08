from django.urls import path
from .views import ListDocuments, addDocs

app_name = 'Documents'

urlpatterns = [
    path('', ListDocuments, name="ListDocuments_urls"),
    path('add/', addDocs, name="newDocuments_urls"),

]
