"""
Django command to wait for the expiring subscriptions.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Subscription
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Expires subscriptions that are past their valid until date.'

    def handle(self, *args, **options):
        now = timezone.now()
        expired_subscriptions = Subscription.objects.filter(valid_until__lt=now).exclude(subscription_plan='Expired') # noqa
        count = expired_subscriptions.update(subscription_plan='Expired')
        self.stdout.write(self.style.SUCCESS(f'Successfully expired {count} subscriptions')) # noqa
        logger.info(f'Successfully expired {count} subscriptions')
