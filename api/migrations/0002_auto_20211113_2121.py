# Generated by Django 3.2.9 on 2021-11-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
