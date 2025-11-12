from rest_framework import serializers
from .models import UserTask
from authentication.serializers import UserSerializer
from authentication.models import CreateUser


class TaskSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CreateUser.objects.all(),
    )

    class Meta:
        model = UserTask
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        users = validated_data.pop("users", [])

        task = UserTask.objects.create(**validated_data)

        task.users.set(users)

        return task
