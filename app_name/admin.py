from django.contrib import admin
from django import forms
from .models import SubjectModel

class SubjectModelAdminForm(forms.ModelForm):

    class Meta:
        model = SubjectModel
        fields = '__all__'


class SubjectModelAdmin(admin.ModelAdmin):
    form = SubjectModelAdminForm
    list_display = ['name', 'code', 'branch', 'units']
    readonly_fields = ['name', 'code', 'branch', 'units']

admin.site.register(SubjectModel, SubjectModelAdmin)


