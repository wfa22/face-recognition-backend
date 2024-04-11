from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from .models import User # noqa
from django.contrib.auth import get_user_model


@receiver(social_account_added)
def create_user_from_social_account(sender, request, sociallogin, **kwargs):
    user_data = sociallogin.account.extra_data
    email = user_data.get('email')
    name = user_data.get('name', '')

    user, created = get_user_model().objects.create_user(
        email=email,
        defaults={
            'name': name,
        }
    )

    if created:
        user.set_unusable_password()
        user.save()

    sociallogin.user = user
    sociallogin.state['user'] = user
