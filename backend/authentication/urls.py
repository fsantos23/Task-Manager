from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
	path('register/', views.RegisterUser.as_view()),
	path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
]

urlpatterns = format_suffix_patterns(urlpatterns)