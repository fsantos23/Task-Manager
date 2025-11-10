from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    TokenObtainLifetimeSerializer,
    TokenRefreshLifetimeSerializer,
)
from rest_framework_simplejwt.views import TokenViewBase

from .serializers import UserSerializer
from utils import logger


# Create your views here.
class UserView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                logger.info(f"User created succesfully: {serializer.data}")
                return Response(serializer.data, status=201)
            logger.warning(f"Error creating user: {serializer.errors}")
            return Response(serializer.errors, status=400)
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            return Response({"error": str(e)}, status=500)

    def patch(self, request):
        try:
            user = request.user

            serializer = UserSerializer(
                instance=user,
                data=request.data,
                partial=True,
            )

            if serializer.is_valid():
                serializer.save()
                logger.info(f"User updated succesfully: {serializer.data}")
                return Response(serializer.data, status=200)

            logger.warning(f"Error updating user: {serializer.errors}")
            return Response(serializer.errors, status=400)
        except Exception as e:
            logger.error(f"Error updating user: {e}")
            return Response(f"Internal server error: {e}", status=500)

    def get(self, request):
        try:
            user = request.user

            serializer = UserSerializer(
                instance=user,
            )
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response(f"Internal server error: {e}", status=500)


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh', '')

            if not refresh_token:
                return Response("No refresh token provided", status=400)

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Successfully logged out", status=200)
        except Exception as e:
            return Response(f"Internal server error: {e}", status=500)


class TokenObtainPairView(TokenViewBase):
    """
    Returns access token, refresh token and expiry time
    """

    serializer_class = TokenObtainLifetimeSerializer


class TokenRefreshView(TokenViewBase):
    """
    Renews token adn returns access token, refresh token and expiry time
    """

    serializer_class = TokenRefreshLifetimeSerializer
