# Generated by Django 4.0.6 on 2022-11-01 10:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_hashtag_post_hashtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likecount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='postlike',
            field=models.ManyToManyField(blank=True, related_name='like_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
