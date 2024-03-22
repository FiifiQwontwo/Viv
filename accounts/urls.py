from django.urls import path
from .views import dashboard, custom_login, student_signup, activate, student_profile, lecturer_profile, \
    lecturer_registration, lecturer_activate

app_name = 'accounts'

urlpatterns = [
    path('', dashboard, name='dashboard_url'),
    path('login/', custom_login, name='login_url'),
    # student
    path('sup/', student_signup, name='student_signup_url'),
    path('student/', student_profile, name='student_profile_url'),
    path('student/activate/<uidb64>/<token>/', activate, name='student_activate_url'),
    # Lecturer profile
    path('lect/', lecturer_profile, name='lect_profile_url'),
    path('lect/signup/', lecturer_registration, name='lecturer_signup_url'),
    path('lect/activate/<uidb64>/<token>/', lecturer_activate, name='lecturer_activate_url'),
]
