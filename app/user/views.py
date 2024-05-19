"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from core.models import User
from user.serializers import (UserSerializer,
                              AuthTokenSerializer,
                              GoogleUserSerializer,
                              GoogleAuthTokenSerializer)

from django.contrib.auth import get_user_model


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

    def get_queryset(self):
        """Return a queryset"""
        return User.objects.all()


class CreateGoogleUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = GoogleUserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')

        # Check if the user with the given email already exists
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            # Return HTTP 200 status without creating a new user
            return Response(
                {'message': 'User with this email already exists.'},
                status=status.HTTP_200_OK)

        # If the user does not exist, proceed with the normal create flow
        return super().create(request, *args, **kwargs)


class CreateGoogleTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = GoogleAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
