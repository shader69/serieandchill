# Generated by Django 3.0.1 on 2019-12-27 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_comment_release'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='release',
            new_name='postdate',
        ),
    ]
