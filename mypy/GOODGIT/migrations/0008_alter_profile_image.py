# Generated by Django 5.0.3 on 2024-04-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOODGIT', '0007_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
