# Generated by Django 3.1.2 on 2020-10-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0006_auto_20201024_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile')], default='adult', max_length=1000, null=True),
        ),
    ]
