# Generated by Django 2.1.5 on 2019-01-19 12:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0008_auto_20190119_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(blank=True), size=None), blank=True, null=True, size=None),
        ),
    ]
