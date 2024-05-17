"""
Serializers for the subscription API view.
"""
from rest_framework import serializers
from core.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for the subscription object."""

    class Meta:
        model = Subscription
        fields = ['user', 'subscription_plan', 'valid_until', 'app_key']
        extra_kwargs = {
            'user': {'read_only': True},
            'app_key': {'read_only': True},
        }
