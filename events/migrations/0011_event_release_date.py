# Generated by Django 3.0.5 on 2020-06-11 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200608_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]