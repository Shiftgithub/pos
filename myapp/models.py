from django.db import models


class StudentForm(models.Model):
    firstname = models.CharField("Enter first name", max_length=50)
    lastname = models.CharField("Enter last name", max_length=10)
    email = models.EmailField("Enter Email")
    file = models.FileField()  # for creating file input

    class Meta:
        db_table = "student"
