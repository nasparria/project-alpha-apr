# from django.shortcuts import render
from django.views.generic import ListView

from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from tasks.models import Task
# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project_list.html"
    context_object_name = "projects_list"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "projects/project_detail_list.html"
    context_object_name = "projects_detail"

    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])
