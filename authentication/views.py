from rest_framework.generics import GenericAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login, logout
from .models import CustomUser
from .permissions import IsAdminUser
from .serializers import (
    CustomUserSerializer, 
    UserRegistrationSerializer, 
    UserLoginSerializer, 
    ChangePasswordSerializer, 
    ResetPasswordSerializer,
    UserUpdateSerializer
)
from rest_framework import serializers

class UserRegistrationAPIView(GenericAPIView):
    """Vista para registrar nuevos usuarios (solo admin debería usarla)."""
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "Usuario registrado correctamente."},
            status=status.HTTP_201_CREATED
        )


class UserLoginAPIView(GenericAPIView):
    """Vista para iniciar sesión y obtener tokens JWT."""
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        # Iniciar sesión en Django (opcional, útil si quieres usar sesiones además de JWT)
        login(request, user)

        # Generar tokens JWT
        token = RefreshToken.for_user(user)
        data = {
            "user": CustomUserSerializer(user).data,
            "tokens": {"refresh": str(token), "access": str(token.access_token)},
        }
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    """Vista para cerrar sesión (invalida el token de refresco)."""
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Token de refresco requerido."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # Invalida el token
            logout(request)  # Cierra la sesión en Django
            return Response({"message": "Sesión cerrada correctamente."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Token inválido o expirado."}, status=status.HTTP_400_BAD_REQUEST)


class UserInfoAPIView(RetrieveAPIView):
    """Vista para obtener la información del usuario autenticado."""
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordAPIView(GenericAPIView):
    """Vista para que los usuarios cambien su propia contraseña."""
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Contraseña cambiada exitosamente."}, status=status.HTTP_200_OK)


class ResetPasswordAPIView(GenericAPIView):
    """Vista para que el admin resetee la contraseña de un usuario a la predeterminada."""
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Contraseña reseteada a '12345678'."}, status=status.HTTP_200_OK)


class UserUpdateAPIView(UpdateAPIView):
    """Vista para actualizar información del usuario."""
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_object(self):
        # Obtener el ID del usuario a actualizar desde la URL
        user_id = self.kwargs.get('user_id')
        return CustomUser.objects.get(id=user_id)


class UserListAPIView(ListAPIView):
    """Vista para listar todos los usuarios con sus grupos (solo admin puede acceder)."""
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        """Retorna todos los usuarios, incluyendo al admin."""
        return CustomUser.objects.all().order_by('username')


class UserDeleteAPIView(DestroyAPIView):
    """Vista para eliminar usuarios (solo admin puede hacerlo)."""
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        return CustomUser.objects.get(id=user_id)

    def perform_destroy(self, instance):
        # Verificar que el usuario no se elimine a sí mismo
        if instance == self.request.user:
            raise serializers.ValidationError("No puedes eliminar tu propio usuario")
        instance.delete()
