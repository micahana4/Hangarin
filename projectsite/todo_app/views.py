from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Task

class HomePageView(TemplateView):
    template_name = "home.html"

class TaskListView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5