# Generated by Django 3.1.1 on 2020-09-08 00:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0003_auto_20200904_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='twituser',
            name='following',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]