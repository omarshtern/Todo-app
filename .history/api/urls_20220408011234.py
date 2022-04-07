from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("task-list/", views.TaskList, name="task-list")
]
