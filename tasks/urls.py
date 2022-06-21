from django.urls import path

from tasks.views import TasksCreateView


urlpatterns = [
    path("create/", TasksCreateView.as_view(), name="create_task")
]

