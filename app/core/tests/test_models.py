"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from core import models


def create_user(email='test@example.com', password='testpass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = create_user()
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)

    def test_create_subscription_successful(self):
        """Test creating a subscription is successful."""
        user = create_user()
        subscription = models.Subscription.objects.get(user=user)
        self.assertEqual(subscription.subscription_plan, 'Free')
        self.assertIsNotNone(subscription.app_key)

    def test_create_connection_successful(self):
        """Test creating a connection is successful."""
        user = create_user()
        mac = '00:0a:95:9d:68:16'
        connection_time = timezone.now()
        connection = models.Connections.objects.create(
            user=user,
            mac=mac,
            connection_time=connection_time,
        )
        self.assertEqual(connection.user, user)
        self.assertEqual(connection.mac, mac)
        self.assertEqual(connection.connection_time, connection_time)
