from django.shortcuts import render


# Create your views here.
def get_user_agents(request):
    return request.META.get('HTTP_USER_AGENT', '')


def dashboard(request):
    return render(request, 'dashboard.html')


def login(request):
    return render(request, 'login/login.html')
