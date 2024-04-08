from django.shortcuts import render
from .models import Faculty
from accounts.decorators import staff_required


# Create your views here.
@staff_required
def listFaculty(request):
    fac = Faculty.objects.all()
    context = {
        'fac': fac

    }
    return render(request, 'admin/faculty.html', context)
