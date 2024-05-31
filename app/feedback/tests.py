"""
Tests for the Feedback API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Feedback

CREATE_FEEDBACK_URL = reverse('feedback:create-feedback')


def sample_feedback(**params):
    """Create and return a sample feedback."""
    defaults = {
        'name': 'Test User',
        'email': 'test@example.com',
        'issue': 'Test issue description'
    }
    defaults.update(params)
    return Feedback.objects.create(**defaults)


class FeedbackModelTests(TestCase):
    """Test the feedback model."""

    def test_create_feedback(self):
        """Test creating a feedback is successful."""
        feedback = sample_feedback()
        self.assertEqual(feedback.name, 'Test User')
        self.assertEqual(feedback.email, 'test@example.com')
        self.assertEqual(feedback.issue, 'Test issue description')


class PublicFeedbackApiTests(TestCase):
    """Test the public features of the feedback API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_feedback_success(self):
        """Test creating feedback with valid payload is successful."""
        payload = {
            'name': 'Test User',
            'email': 'test@example.com',
            'issue': 'Test issue description'
        }
        response = self.client.post(CREATE_FEEDBACK_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        feedback = Feedback.objects.get(id=response.data['id'])
        self.assertEqual(feedback.name, payload['name'])
        self.assertEqual(feedback.email, payload['email'])
        self.assertEqual(feedback.issue, payload['issue'])

    def test_create_feedback_invalid(self):
        """Test creating feedback with invalid payload fails."""
        payload = {
            'name': '',
            'email': 'notanemail',
            'issue': ''
        }
        response = self.client.post(CREATE_FEEDBACK_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
