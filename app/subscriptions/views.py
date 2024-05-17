"""
Views for the subscription API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from core.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


class ManageSubscriptionView(generics.GenericAPIView):
    """Manage the authenticated users subscription with GET and PUT methods."""
    serializer_class = SubscriptionSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user's subscription."""
        user = self.request.user
        return Subscription.objects.get(user=user)

    def get(self, request, *args, **kwargs):
        """Retrieve the authenticated user's subscription."""
        subscription = self.get_object()
        serializer = self.get_serializer(subscription)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """Update the authenticated user's subscription.'"""
        subscription = self.get_object()
        serializer = self.get_serializer(subscription, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
