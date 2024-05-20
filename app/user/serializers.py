"""
Serializers for the user API view.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.db.migrations import serializer  # noqa
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError

from rest_framework import serializers

from core.models import Country


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        required=False,
    )
    picture = serializers.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name', 'country', 'picture']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs


class GoogleUserSerializer(serializers.ModelSerializer):
    """Serializer for the google user object."""

    picture = serializers.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'picture']

    def create(self, validated_data):
        """Create and return a user."""
        email = validated_data.get('email')

        # Check if the user with the given email already exists
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('User with this email already exists.')

        return get_user_model().objects.create_user(**validated_data)


class GoogleAuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    name = serializers.CharField()

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        name = attrs.get('name')
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        if user.name != name:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs