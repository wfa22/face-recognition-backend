"""
Serializers for the Feedback API view.
"""
from rest_framework import serializers
from core.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """Serializer for the feedback object."""

    class Meta:
        model = Feedback
        fields = ['id', 'name', 'email', 'issue']
        read_only_fields = ['id']
