from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("tasks", views.TasksListView.as_view()),
    path("tasks/<int:task_id>", views.SingleTaskListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
