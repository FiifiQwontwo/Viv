from MySQLdb._exceptions import IntegrityError
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import DocumentUploader
from .models import Document


# Create your views here.


def ListDocuments(request):
    try:
        if request.user.is_staff or request.user.is_lecturer:
            docs = Document.objects.all()
        else:
            docs = Document.objects.filter(student=request.user)

        if not docs.exists() and not (request.user.is_staff or request.user.is_lecturer):
            return render(request, 'docs/docs_list.html', {'docs': docs})

        return render(request, 'docs/docs_list.html', {'docs': docs})
    except Exception as e:
        raise Http404()


def docDetails(request,id):
    try:
        dsdetails = Document.objects.filter(id=id)
        context ={
            'dsdetails': dsdetails
        }
        return render(request,'docs/dosdetails.html', context)
    except Document.DoesNotExist:
        return Http404()
    except Exception as e:
        return Http404(" An error occurred while processing")


def addDocs(request):
    if request.method == 'POST':
        form = DocumentUploader(request.POST, request.FILES)
        if form.is_valid():
            try:
                docs = form.save(commit=False)
                docs.save()
                messages.success(request, 'Document  added  successfully.')
                return redirect('documents:ListDocuments_urls')

            except IntegrityError as e:
                messages.error(request, f'An error occurred while adding the document: {e}')
        else:
            messages.error(request, 'Invalid form data. Please check the field.')

    else:
        form = DocumentUploader()

    context = {
        'form': form,
    }

    return render(request, 'docs/adddocs.html', context)
