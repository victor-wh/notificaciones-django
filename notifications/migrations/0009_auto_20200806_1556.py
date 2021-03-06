# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-08-06 20:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_index_together_recipient_unread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
