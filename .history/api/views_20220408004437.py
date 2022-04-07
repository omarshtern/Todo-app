from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

@api_view(["GET"])

def apiOverview(request):
    api_urls = {
        "List" : "/task-list",
        "Detail View": "/task-detail/<str:pk>/",
        "Create": "/task-create/",
        "Update": "/task-update/",
        "Delete": "/task-delete/<str:pk>/",
    }

    return Response(api_urls)

@api_view(["GET"])

def TaskList(request):
    tasks = Task.objects.all().order_by("-id")
    