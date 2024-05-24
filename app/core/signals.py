"""
Signals for our project.
"""
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings  # noqa
from core.models import User
import os


@receiver(post_delete, sender=User)
def delete_user_picture(sender, instance, **kwargs):
    """Deletes users picture after user is deleted."""
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)
