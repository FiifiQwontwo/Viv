from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def staff_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden("You are not allowed to view this")
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def student_required(view_function):
    def wrapper_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_student:
            return HttpResponseForbidden("You are not allowed to view")
        return view_function(request, *args, **kwargs)

    return wrapper_view


def lecturer_required(view_function):
    def wrapper_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_lecturer:
            return HttpResponseForbidden("You are not allowed to view")
        return view_function(request, *args, **kwargs)

    return wrapper_view
