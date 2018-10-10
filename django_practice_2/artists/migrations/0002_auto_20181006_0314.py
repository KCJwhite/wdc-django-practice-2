# Generated by Django 2.0 on 2018-10-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('Soul', 'Soul'), ('Pop', 'Pop')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artistic_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]