from django.db import models

from authentication.models import User


# Create your models here.
class TaskBase(models.Model):
	title = models.CharField(null=False, max_length=256)
	description = models.CharField(null=False)

	is_completed = models.BooleanField(default=False)
	due_date = models.DateTimeField(null=True, blank=True)

	class Priority(models.TextChoices):
		LOW = "Low"
		NORMAL = "Normal"
		HIGH = "High"
	
	priority_level = models.CharField(
		max_length=10,
		choices=Priority.choices,
		default=Priority.NORMAL
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
		ordering = ['-create_at']

	def __str__(self):
		return self.title
	
class UserTask(TaskBase):

	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='tasks',
	)

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'User Task'
		verbose_name_plural = 'User Tasks'

	def __str__(self):
		return f"{self.user.username} - {self.title}"