# Generated by Django 5.0.1 on 2024-02-04 17:22

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOODGIT', '0003_remove_profile_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_create',
            field=models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
