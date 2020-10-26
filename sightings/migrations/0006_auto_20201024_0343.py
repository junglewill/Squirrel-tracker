# Generated by Django 3.1.2 on 2020-10-24 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0005_squirrel_latitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='id',
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Unique_Squirrel_ID',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]