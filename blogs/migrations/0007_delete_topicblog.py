# Generated by Django 5.2.1 on 2025-06-13 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_rename_title_topicblog_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TopicBlog',
        ),
    ]
