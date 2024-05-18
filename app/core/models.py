"""
Database models.
"""
from django.contrib.admin import ModelAdmin  # noqa
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from datetime import datetime
from django.utils import timezone
import secrets
from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        user.is_staff = True
        user.save(using=self._db)

        return user


class Country(models.Model):
    """Country table."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    username = None
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    is_staff = models.BooleanField(default=False)

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
    mac = models.CharField(max_length=50)
    connection_time = models.DateTimeField()


@receiver(post_save, sender=SocialAccount)
def create_profile(sender, instance, created, **kwargs):
    if created:
        data = instance.extra_data
        user = instance.user
        name = data['name']
        user.name = name

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
        user.save()


class Feedback(models.Model):
    """Feedback model."""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    issue = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
