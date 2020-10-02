from django import forms
from .models import SubjectModel


class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = SubjectModel
        fields = ['name', 'code', 'branch', 'units', 'user']


