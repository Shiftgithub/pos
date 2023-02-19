from django.shortcuts import render
from file_upload.models import FileUploadModel
from .forms import FileUploadForm


def FileUpload(request):
    form = FileUploadForm()
    return render(request, "file_upload/file.html", {'form': form})
