# Generated by Django 4.0.6 on 2022-11-01 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_likecount_post_postlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likecount',
            new_name='like_count',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postlike',
            new_name='post_like',
        ),
    ]