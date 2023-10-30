from django.urls import path
from notebook import views
from notebook.views import (
    TaskListView,
    TagsCreateView,
    TagsUpdateView,
    TaskUpdateView,
    TaskCreateView,
    TagsDeleteView,
    CompletionTaskView,
    TagsListView,
    TaskDeleteView,
)

urlpatterns = [
    path("", views.home_page, name="task-list"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),

    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

    path("task/<int:pk>/completion/", CompletionTaskView.as_view(), name="completion"),
    path("task/add/", views.add_task, name="create_task"),
    path("tags/add/", views.add_tag, name="create_tag"),

]

app_name = "notebook"
