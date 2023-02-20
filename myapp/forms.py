from django import forms
from myapp.models import StudentForm


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentForm
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    # firstname = forms.CharField(label="Enter first name", max_length=50)
    # lastname = forms.CharField(label="Enter last name", max_length=10)
    # email = forms.EmailField(label="Enter Email")
    # file = forms.FileField()  # for creating file input
