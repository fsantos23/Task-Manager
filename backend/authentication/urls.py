from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

urlpatterns = [
    path("user", views.UserView.as_view(), name='register_user'),
    path("login", views.TokenObtainPairView.as_view(), name="token_obtain"),
    path("logout", views.LogoutUser.as_view(), name='logout_user'),
    path(
        "token/refresh", views.TokenRefreshView.as_view(), name='refresh_token'
    ),
    path("token/verify", TokenVerifyView.as_view(), name='verify_token'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
