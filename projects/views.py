from django.shortcuts import render
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project
from datetime import datetime
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
import pdb

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    model = Project
    Project.objects.order_by().filter()
    template_name = 'projects/project_create.html'
    fields = '__all__'
    success_url = reverse_lazy('project_list')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    context_object_name = 'project'
    fields = '__all__'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project_list')