# Generated by Django 3.1.1 on 2021-03-29 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes',
        ),
    ]
