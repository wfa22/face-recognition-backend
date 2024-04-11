from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.http import HttpRequest
from allauth.socialaccount.models import SocialLogin

from .models import User


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_or_create_user(self, request, sociallogin):
        user_data = sociallogin.account.extra_data
        email = user_data.get('email')
        name = user_data.get('name', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            sociallogin.user = user
            sociallogin.state['user'] = user
        else:
            user = User.objects.create_user(email=email, name=name)

        return user

    def is_open_for_signup(
            self,
            request: HttpRequest,
            sociallogin: SocialLogin = None) -> bool:
        """
        Checks whether signup is allowed for the current request.
        """
        return True
