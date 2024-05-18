"""
Views for the Feedback API.
"""
from .serializers import FeedbackSerializer
from rest_framework import generics, permissions


class CreateFeedbackView(generics.CreateAPIView):
    """Create a new feedback."""
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]
