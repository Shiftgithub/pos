from django import forms
from file_upload.models import FileUploadModel

class FileUploadForm(forms.ModelForm):
    class Meta:
        models = FileUploadModel()
        fields = "__all__"

        