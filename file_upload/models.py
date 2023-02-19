from django.db import models


class FileUploadModel(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()

    class Meta:
        db_table = "fileupload"