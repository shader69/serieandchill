# Generated by Django 3.0.1 on 2019-12-27 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20191227_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='postdate',
        ),
    ]