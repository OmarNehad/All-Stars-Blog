# Generated by Django 3.0.5 on 2020-06-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20200613_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventvideos',
            name='video',
            field=models.FileField(upload_to='videos'),
        ),
    ]
