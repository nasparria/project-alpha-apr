# from django.shortcuts import render
from django.views.generic.edit import CreateView
# from django.views.generic import ListView
from tasks.models import Task
# from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.


class TasksCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])


# ---------------------------------------------------------
# class ProjectCreateView(LoginRequiredMixin, CreateView):
#     model = Project
#     template_name = "projects/create.html"
#     fields = ["name", "description", "members"]

#     def get_success_url(self):
#         return reverse_lazy("show_project", args=[self.object.id])
