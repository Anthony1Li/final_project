# Generated by Django 2.2.7 on 2019-11-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('unqiue_squirrel_id', models.CharField(max_length=200)),
                ('shift', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('age', models.CharField(max_length=200)),
                ('primary_fur_color', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('specific_location', models.CharField(max_length=200)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('other_activities', models.CharField(max_length=200)),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
            ],
        ),
    ]
