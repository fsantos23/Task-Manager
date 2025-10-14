from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

import logging
from .models import User

# Create your views here.
class RegisterUser(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		try:
			username = request.data.get('username', '')
			password = request.data.get('password')
			email = request.data.get('email')

			if not email or not password:
				return Response({'error': "No email or password provided"}, status=400)

			if User.objects.filter(email=email).exists():
				return Response({'error': "Email already exists"}, status=400)

			user = User.objects.create_user(
				username=username,
				password=password,
				email=email,
			)

			refresh = RefreshToken.for_user(user)

			logging.info(f"User {username} created succesfully")
			return Response({
				'message': 'User Created succesfully',
				'tokens': {
					'refresh': str(refresh),
					'access': str(refresh.access_token),
				}
			}, status=201)
		except Exception as e:
			logging.error(f"Error creating user: {str(e)}")
			return Response({'error': str(e)}, status=500)