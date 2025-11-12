from django.db import models

from authentication.models import CreateUser


# Create your models here.
class TaskBase(models.Model):
    title = models.CharField(null=False, max_length=256)
    content = models.CharField(null=True)

    is_completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)

    class Priority(models.TextChoices):
        LOW = "low"
        NORMAL = "normal"
        HIGH = "high"

    priority_level = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.NORMAL
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class UserTask(TaskBase):

    users = models.ManyToManyField(
        CreateUser,
        related_name="tasks"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "User Task"
        verbose_name_plural = "User Tasks"

    def __str__(self):
        user_count = self.users.count()
        if user_count == 1:
            return f"{self.users.first().username} - {self.title}"
        else:
            return f"{user_count} users - {self.title}"
