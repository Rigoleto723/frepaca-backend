from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, UserInfoAPIView, ChangePasswordAPIView, ResetPasswordAPIView, UserUpdateAPIView, UserListAPIView, UserDeleteAPIView

urlpatterns = [
    # Endpoints personalizados con APIView
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/', UserInfoAPIView.as_view(), name='user-info'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('user/<int:user_id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/<int:user_id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]
