# Generated by Django 2.1.5 on 2019-02-22 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_tweetdetails_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetdetails',
            name='created_by',
        ),
    ]
