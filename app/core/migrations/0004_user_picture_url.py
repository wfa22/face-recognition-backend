# Generated by Django 5.0 on 2024-05-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
