from django.urls import path, include
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, UserInfoAPIView, ChangePasswordAPIView, ResetPasswordAPIView, UserUpdateAPIView, UserListAPIView, UserDeleteAPIView

urlpatterns = [
    # Endpoints personalizados con APIView
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('users/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('users/logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('users/info/', UserInfoAPIView.as_view(), name='user-info'),
    path('users/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('users/reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('users/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]
