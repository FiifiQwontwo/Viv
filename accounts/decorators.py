from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def user_is_staff(user):
    return user.is_authenticated and user.is_staff


def staff_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_authenticated:
            return HttpResponseForbidden("You are not allowed to view this")
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def student_required(view_fuction):
    def wrapper_view(request, *args, **kwargs):
        if not request.user.is_student or not request.user.is_authenticated:
            return HttpResponseForbidden("You are not allowed to view")
        return view_fuction(request, *args, **kwargs)

    return wrapper_view


def lecturer_required(view_function):
    def wrapper_view(request, *args, **kwargs):
        if not request.user.is_lecturer or not request.user.is_authenticated:
            return HttpResponseForbidden("You are not allowed to view")
        return view_function(request, *args, **kwargs)

    return wrapper_view


