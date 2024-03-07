from django.urls import path
from .views import dashboard, login
app_name = 'accounts'

urlpatterns = [
    path('', dashboard, name='dashboard_url'),
    path('login/', login, name='login_ur'),

]