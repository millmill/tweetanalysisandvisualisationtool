# Generated by Django 2.1.7 on 2019-02-28 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0023_auto_20190228_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetdetails',
            name='screen_name',
        ),
    ]
