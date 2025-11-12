import django_filters
from .models import UserTask
from authentication.models import CreateUser


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title', lookup_expr="icontains"
    )
    content = django_filters.CharFilter(
        field_name='content', lookup_expr="icontains"
    )
    is_completed = django_filters.BooleanFilter(field_name='is_completed')
    priority_level = django_filters.ChoiceFilter(
        choices=UserTask.Priority.choices
    )
    users = django_filters.ModelMultipleChoiceFilter(
        queryset=CreateUser.objects.all()
    )

    class Meta:
        model = UserTask
        fields = [
            "users",
            "title",
            "content",
            "is_completed",
            "priority_level",
        ]
