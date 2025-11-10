from django.contrib import admin
from .models import CreateUser
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.token_blacklist.admin import (
    OutstandingTokenAdmin,
)


# Register your models here.


@admin.register(CreateUser)
class CreateUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

    fields = ["username", "email", "password"]


admin.site.unregister(OutstandingToken)  # Unregister for Custom admin page


@admin.register(OutstandingToken)
class CustomOutstandingToken(OutstandingTokenAdmin):
    list_display = ("id", "get_username", "jti", "created_at", "expires_at")

    def get_username(self, obj):
        return obj.user.username if obj.user else "No User"

    get_username.short_description = "Username"
