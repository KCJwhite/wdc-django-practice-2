# Generated by Django 2.0 on 2018-10-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_auto_20181008_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop')], max_length=255, null=True),
        ),
    ]
