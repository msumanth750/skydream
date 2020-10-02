from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import SubjectModel
from .forms import SubjectModelForm


class SubjectModelListView(ListView):
    model = SubjectModel


class SubjectModelCreateView(CreateView):
    model = SubjectModel
    form_class = SubjectModelForm


class SubjectModelDetailView(DetailView):
    model = SubjectModel


class SubjectModelUpdateView(UpdateView):
    model = SubjectModel
    form_class = SubjectModelForm

