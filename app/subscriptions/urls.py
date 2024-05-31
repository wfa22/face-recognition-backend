"""
URL mappings for the subscription API.
"""
from django.urls import path
from subscriptions import views

app_name = 'subscriptions'

urlpatterns = [
    path('subscription/',
         views.ManageSubscriptionView.as_view(),
         name='manage-subscription'
         ),
]
