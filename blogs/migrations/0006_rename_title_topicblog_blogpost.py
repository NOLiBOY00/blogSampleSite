# Generated by Django 5.2.1 on 2025-06-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_rename_text_topicblog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicblog',
            old_name='title',
            new_name='blogpost',
        ),
    ]
