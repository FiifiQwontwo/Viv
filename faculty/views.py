from django.http import Http404
from django.shortcuts import render, get_object_or_404
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


def detailsFaculty(request, slug):
    facs = get_object_or_404(Faculty, slug=slug)
    if facs is None:
        raise Http404()
    return render(request, 'admin/facultydetails.html', {'fac': facs})
