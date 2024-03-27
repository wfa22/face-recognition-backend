"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from datetime import datetime
from django.utils import timezone
import secrets


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        while True:
            app_key = secrets.token_hex(10)
            if not Subscription.objects.filter(app_key=app_key).exists():
                break

        Subscription.objects.create(
            user=user,
            subscription_plan='Free',
            valid_until=timezone.make_aware(datetime.max),
            app_key=app_key,
        )

        return user

    def create_superuser(self, email, password):
        """Create and return new superuser."""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Country(models.Model):
    """Country table."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Subscription(models.Model):
    """Subscription object."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    subscription_plan = models.CharField(max_length=100)
    valid_until = models.DateTimeField()
    app_key = models.CharField(max_length=50, null=True)


class Connections(models.Model):
    """User's connections object."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Mac = models.CharField(max_length=50)
    connection_time = models.DateTimeField()
