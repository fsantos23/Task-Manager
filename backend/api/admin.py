from django.contrib import admin
from .models import UserTask

# Register your models here.


@admin.register(UserTask)
class UsersTaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "get_usernames",
        "title",
        "due_date",
        "priority_level",
        "created_at",
    )

    def get_usernames(self, obj):
        users = obj.users.all()

        if not users:
            return "No users"

        return ", ".join([user.username for user in users])

    get_usernames.short_description = "Users"
