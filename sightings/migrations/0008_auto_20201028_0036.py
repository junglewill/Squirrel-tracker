# Generated by Django 3.1.2 on 2020-10-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0007_auto_20201027_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
