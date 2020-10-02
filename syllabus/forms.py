from django import forms
from .models import SubjectModel

class SubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectModel
        fields ="__all__"
