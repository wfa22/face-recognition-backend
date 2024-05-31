"""
URL mappings for the Feedback API.
"""

from django.urls import path
from .views import CreateFeedbackView

app_name = 'feedback'

urlpatterns = [
    path('feedback/', CreateFeedbackView.as_view(), name='create-feedback'),
]
