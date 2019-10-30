from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Category, Project
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("planner-namespace:index")


class DetailView(generic.DetailView):
    model = Task
    template_name = "planner/detail.html"



class ProjectView(generic.ListView):
    template_name = "planner/project.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

 

@method_decorator(login_required, name='dispatch')
class ProjectsListed(generic.ListView):
    template_name = "planner/projects_listed.html"
    context_object_name = "project_list"

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)



class DashboardView(generic.ListView):
    template_name = "dashboard/index.html"

    def get_queryset(self):
        return HttpResponse("")

# class IndexView(generic.ListView):
#     template_name = "planner/index.html"
#     # context_object_name = "task_list"
#     context_object_name = "category_list"
#
#     def get_queryset(self):
#         # return Task.objects.all()
#         return Category.objects.all()


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("planner-namespace:project_page")


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("planner-namespace:project_page")


class CategoryCreate(CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("planner-namespace:project_page")



