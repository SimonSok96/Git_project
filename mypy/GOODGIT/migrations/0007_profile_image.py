# Generated by Django 5.0.3 on 2024-04-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOODGIT', '0006_rename_author_tweet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
