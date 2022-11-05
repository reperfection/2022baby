# Generated by Django 4.0.6 on 2022-11-01 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_comment_comment_text_alter_comment_postid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='posts.hashtag'),
        ),
    ]