# Generated by Django 2.1.2 on 2018-12-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0005_auto_20181208_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='id',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='id',
            name='gender',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='id',
            name='q1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='id',
            name='q2',
            field=models.BooleanField(default=False),
        ),
    ]
