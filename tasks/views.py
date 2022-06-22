# from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
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


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "tasks_list"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TasksUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/edit.html"
    context_object_name = "tasks_edit"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")

    # def get_success_url(self):
    #     return reverse_lazy("show_my_tasks", args=[self.object.id])


# ------------------------------------------------------
# class ProjectListView(LoginRequiredMixin, ListView):
#     model = Project
#     template_name = "project_list.html"
#     context_object_name = "projects_list"

#     def get_queryset(self):
#         return Project.objects.filter(members=self.request.user)
