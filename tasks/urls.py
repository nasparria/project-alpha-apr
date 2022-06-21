from django.urls import path

from tasks.views import TasksCreateView, TasksListView, TasksUpdateView


urlpatterns = [
    path("create/", TasksCreateView.as_view(), name="create_task"),
    path("mine/", TasksListView.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete/", TasksUpdateView.as_view(), name="complete_task"),
]

