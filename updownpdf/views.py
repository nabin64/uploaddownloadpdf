from django.shortcuts import render, redirect
from myapp.forms import PDFFileForm
from myapp.models import *

    
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from myapp.models import PDFFile


def HOME(request):
    return render(request,'base.html')

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'upload_pdf.html')
    else:
        form = PDFFileForm()
    return render(request, 'upload_pdf.html', {'form': form})
def pdf_list(request):
    pdf_files = PDFFile.objects.all()
 
    return render(request, 'pdf_list.html', {'pdf_files': pdf_files})


def DownloadPDF(request, pdf_id):
    pdf_file = get_object_or_404(PDFFile, id=pdf_id)
    response = HttpResponse(pdf_file.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf_file.name}.pdf"'
    return response