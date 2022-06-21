from django.urls import path

from tasks.views import TasksCreateView, TasksListView


urlpatterns = [
    path("create/", TasksCreateView.as_view(), name="create_task"),
    path("mine/", TasksListView.as_view(), name="show_my_tasks"),
]

