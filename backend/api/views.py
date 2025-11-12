from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import UserTask
from .serializers import TaskSerializer
from .filters import TaskFilter
from utils import logger

# Create your views here.


class TasksListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            query = UserTask.objects.all()
            filterset = TaskFilter(request.GET, queryset=query)
            if filterset.is_valid():
                query = filterset.qs

            paginator = PageNumberPagination()
            paginator.page_size = 50
            paginated_queryset = paginator.paginate_queryset(query, request)

            serializer = TaskSerializer(paginated_queryset, many=True)

            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            logger.error(f"Error getting tasks {e}")
            return Response(f"Internal server error: {e}", status=500)

    def post(self, request):
        try:
            serialized = TaskSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                logger.info(f"Task created succesfully: {serialized.data}")
                return Response(serialized.data, status=201)

            logger.warning(f"Error creating task: {serialized.errors}")
            return Response(serialized.errors, status=400)
        except Exception as e:
            logger.error(f"Error creating task {e}")
            return Response(f"Internal Server Error: {e}", status=500)


class SingleTaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        try:

            serializer = TaskSerializer(
                instance=task_id,
            )

            if serializer.is_valid():
                logger.info(f"Got single task successfully")
                return Response(serializer.data, status=200)
            logger.warning(f"Error getting the task: {serializer.errors}")
            return Response(serializer.errors, status=400)
        except Exception as e:
            logger.error(f"Error getting task {e}")
            return Response(f"Internal Server Error: {e}", status=500)

    def patch(self, request, task_id):
        try:

            serializer = TaskSerializer(
                instance=task_id,
                data=request.data,
                partial=True,
            )

            if serializer.is_valid():
                serializer.save()
                logger.info(f"Task updated successfully: {serializer.data}")
                return Response(serializer.data, status=200)
            logger.warning(f"Error updating task: {serializer.errors}")
            return Response(serializer.errors, status=400)
        except Exception as e:
            logger.error(f"Error updating task {e}")
            return Response(f"Internal Server Error: {e}", status=500)

    def delete(self, request, task_id):
        try:

            task = UserTask.objects.get(id=task_id)

            if task:
                task.delete()
                logger.info("Successfully deleted task")
                return Response(f"Deleted task {task_id}", status=204)
            logger.warning(f"No task to delete: {task_id}")
            return Response("No task to delete", status=400)
        except Exception as e:
            logger.error(f"Error deleting user: {e}")
            return Response(f"Internal server error: {e}", status=500)
