from django.shortcuts import render
from .models import SubjectModel
from . import forms

# Create your views here.
def indexView(request):
    form = forms.SubjectForm()
    subjects = SubjectModel.objects.all()
    if request.method == 'POST':
        form = forms.SubjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        subjects = SubjectModel.objects.all()
        form = forms.SubjectForm()
        return render(request,'syllabus/index.html',{'subjects':subjects,'form':form})
    return render(request,'syllabus/index.html',{'subjects':subjects,'form':form})
