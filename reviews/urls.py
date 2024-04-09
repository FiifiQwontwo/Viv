from django.urls import path
from .views import create_review, list_reviews


app_name= 'reviews'

urlpatterns =[
       path('list/', list_reviews, name='list_review_url'),
       path('add/<int:document_id>', create_review, name='create_review_url'),
]
