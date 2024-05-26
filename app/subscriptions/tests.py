"""
Tests for the subscription API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Subscription
from subscriptions.serializers import SubscriptionSerializer

MANAGE_SUBSCRIPTION_URL = reverse('subscriptions:manage-subscription')


def create_user(email='test@example.com', password='testpass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password)


class PublicSubscriptionApiTest(TestCase):
    """Test API requests that do not require authentication."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_subscription_unauthorized(self):
        """Test that authentication is required for retrieving subscription."""
        res = self.client.get(MANAGE_SUBSCRIPTION_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_subscription_unauthorized(self):
        """Test that authentication is required for updating a subscription."""
        res = self.client.put(MANAGE_SUBSCRIPTION_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateSubscriptionApiTest(TestCase):
    """Test API requests that require authentication."""

    def setUp(self):
        self.user = create_user(
            email='test@example.com',
            password='testpass123',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_subscription_success(self):
        """Test retrieving subscription for logged in user."""
        res = self.client.get(MANAGE_SUBSCRIPTION_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        subscription = Subscription.objects.get(user=self.user)
        serializer = SubscriptionSerializer(subscription)
        self.assertEqual(res.data, serializer.data)

    def test_update_subscription_success(self):
        """Test updating the subscription for the authenticated user."""
        payload = {'subscription_plan': 'Paid',
                   'valid_until': '2024-05-17T17:01:02.206Z',
                   }
        res = self.client.put(MANAGE_SUBSCRIPTION_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        subscription = Subscription.objects.get(user=self.user)
        self.assertEqual(subscription.subscription_plan,
                         payload['subscription_plan']
                         )
