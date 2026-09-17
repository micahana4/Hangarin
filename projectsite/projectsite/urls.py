"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_app.views import HomePageView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from todo_app.views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView
from todo_app.views import SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView
from todo_app.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from todo_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/add', TaskCreateView.as_view(), name='task-add'),
    path('tasks/<pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),

    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/add', NoteCreateView.as_view(), name='note-add'),
    path('notes/<pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'),

    path('subtasks/', views.SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add', views.SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtasks/<pk>/', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtasks/<pk>/delete', views.SubTaskDeleteView.as_view(), name='subtask-delete'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
]