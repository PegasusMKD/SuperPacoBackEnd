# Generated by Django 2.1.2 on 2018-12-08 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leftovers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_choices', models.PositiveIntegerField()),
                ('neutral_choices', models.PositiveIntegerField()),
                ('bad_choices', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='id',
            name='activity',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='bad_choices',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='id',
            name='good_choices',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='id',
            name='neutral_choices',
            field=models.PositiveIntegerField(),
        ),
    ]
