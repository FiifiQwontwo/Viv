from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django_user_agents.utils import get_user_agent

from course.models import Course
from djangoProject12 import settings
from .forms import StudentRegistrationForm
from .models import Student, UserAgentInfo


# Create your views here.
def get_user_agents(request):
    return request.META.get('HTTP_USER_AGENT', '')


def dashboard(request):
    return render(request, 'dashboard.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login successful')
                user_agent = get_user_agents(request)

                request.session['is_mobile'] = 'Mobile' in user_agent

                if user.is_student:
                    return redirect('accounts:student_profile_url')
                elif user.is_lecturer:
                    return redirect('accounts:lect_profile_url')
                elif user.is_staff:
                    return redirect('accounts:dashboard_url')
            else:
                messages.error(request, 'Your Account is not Active')
        else:
            messages.error(request, 'Invalid Credentials')

    return render(request, 'login/login.html')


def student_signup(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()

            student = Student.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                index_number=form.cleaned_data['index_number'],
                phone=form.cleaned_data['phone'],
                course=form.cleaned_data['course'],
                level=form.cleaned_data['level'],
                # slug=form.cleaned_data['slug'],

            )

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            current_site = get_current_site(request)
            email = form.cleaned_data['email']
            html_template = 'verification.html'
            html_message = render_to_string(html_template, {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),

            })
            mail_subject = "Account Activation"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(mail_subject, html_message, email_from, recipient_list)
            message.content_type = "html"
            message.send()

            messages.success(request, 'Signup successful. Check your mail for verification')
            return redirect('/accounts/login/?command=verification&email=' + email)
    else:
        form = StudentRegistrationForm()
        courses = Course.objects.all()  # Retrieve all courses from the database

    return render(request, 'login/student_signup.html', {'form': form})


def student_profile(request):
    return render(request, 'login/studentprofile.html')


def lecturer_profile(request):
    return render(request, 'login/lecturerprofile.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        User = get_user_model()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('accounts:login_url')
    else:
        messages.error(request, 'Invalid activation Link.')
        return redirect('accounts:student_signup_url')
