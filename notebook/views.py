from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from notebook.models import Task, Tag
from notebook.forms import TaskForm, TagForm


def home_page(request) -> None:
    tasks = Task.objects.all()
    return render(request, "notebook/task_list.html", {"tasks": tasks, "current-path": request.path})


def add_task(request) -> None:
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notebook:task-list")
    else:
        form = TaskForm
    return render(request, "notebook/create_task.html", {"form": form})


def add_tag(request) -> None:
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notebook:tags-list")
    else:
        form = TagForm
    return render(request, "notebook/create_tag.html", {"form": form})


class TaskListView(generic.ListView):
    model = Task

    @staticmethod
    def get(request, *args, **kwargs) -> None:
        tasks = Task.objects.order_by('-is_done', '-created')
        return render(request, "notebook/task_list.html", {"tasks": tasks})


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("notebook:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("notebook:task-list")
    fields = "__all__"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("notebook:task-list")
    template_name = "notebook/task_confirm_delete.html"


class TagsListView(generic.ListView):
    model = Tag

    def get(self, request: HttpRequest) -> HttpResponse:
        tags = Tag.objects.all()
        return render(request, "notebook/tags_list.html", {"tags": tags})


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("notebook:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("notebook:tags-list")
    fields = "__all__"


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "notebook/tags_confirm_delete.html"
    success_url = reverse_lazy("notebook:tags-list")


class CompletionTaskView(generic.View):
    @staticmethod
    def get(request, pk) -> None:
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse("notebook:task-list"))
