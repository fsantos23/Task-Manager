from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserTask

from pprint import pprint

# Create your views here.
class Private(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request):
		print("You are on a private endpoint now!!!!!")
		return Response({  # ← Add this!
            'message': 'You are on a private endpoint!',
            'user': request.user.email
        })
	
class Tasks(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		"""Get's and returns all the users tasks"""
		try:
			user = request.user
			tasks = UserTask.objects.filter(user=user)

			pprint(tasks)

			return Response(tasks, status=200)
		except Exception as e:
			return Response(f"Internal Server error: {e}", status=500)

	def post(self, request):
		"""Creates a task"""
		pass
