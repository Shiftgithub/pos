from django import forms
from django.core.exceptions import ValidationError

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'nid')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'phone': forms.TextInput(attrs={"class": "form-control mb-5"}),
            'email': forms.TextInput(attrs={"class": "form-control mb-5"}),
            'nid': forms.TextInput(attrs={"class": "form-control mb-5"}),
        }
        # labels = {
        #     'text': 'Write your thoughts'
        # }
