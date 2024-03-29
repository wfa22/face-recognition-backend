"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

class SubscriptionAdmin(admin.ModelAdmin):
    """Define the admin pages for Subscriptions."""
    ordering = ['user_id']
    list_display = ['user', 'subscription_plan', 'valid_until', 'app_key']
    readonly_fields = ['user', 'app_key']
    fieldsets = (
        (None, {'fields': ('user', 'subscription_plan', 'app_key')}),
        (_('Subscription Details'), {'fields': ('valid_until',)}),
    )


class CountryAdmin(admin.ModelAdmin):
    """Define the admin pages for Countries."""
    ordering = ['id']
    list_display = ['name']
    fieldsets = (
        (None, {'fields': ('name',)}),
    )


class ConnectionsAdmin(admin.ModelAdmin):
    """Define the admin pages for Connections."""
    ordering = ['connection_time']
    list_display = ['user', 'mac', 'connection_time']
    readonly_fields = ['user','connection_time','mac']
    fieldsets = (
        (None, {'fields': ('user', 'mac')}),
        (_('Connection Details'), {'fields': ('connection_time',)}),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Subscription, SubscriptionAdmin)
admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.Connections, ConnectionsAdmin)