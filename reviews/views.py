from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from document.models import Document
from .models import Review
from .forms import ReviewUploads


# Create your views here.

@login_required
def create_review(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.user.is_lecturer:
        if request.method == 'POST':
            form = ReviewUploads(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.document = document
                review.reviewer = request.user
                review.save()
                return redirect('document_detail', document_id=document_id)
        else:
            form = ReviewUploads()

        return render(request, 'create_review.html', {'form': form, 'document': document})
    else:
        # If the logged-in user is not a lecturer, redirect to a different page or show an error message
        return redirect('document_detail', document_id=document_id)
