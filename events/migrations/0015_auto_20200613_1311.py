# Generated by Django 3.0.5 on 2020-06-13 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20200613_1300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventImages',
            new_name='EventImage',
        ),
        migrations.RenameModel(
            old_name='EventVideos',
            new_name='EventVideo',
        ),
    ]
