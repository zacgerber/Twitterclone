# Generated by Django 3.1.1 on 2020-09-03 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twituser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='twituser',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='twituser',
            name='homepage',
        ),
    ]
