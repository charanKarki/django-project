# Generated by Django 2.2 on 2019-06-30 09:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myApp',
            new_name='post',
        ),
    ]
