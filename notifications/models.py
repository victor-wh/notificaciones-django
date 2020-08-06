from swapper import swappable_setting

from .base.models import AbstractNotification, notify_handler  # noqa
from django.db import models
from django.conf import settings

class Notification(AbstractNotification):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='notifications',
        on_delete=models.SET_NULL
        )

    class Meta(AbstractNotification.Meta):
        abstract = False
        swappable = swappable_setting('notifications', 'Notification')
