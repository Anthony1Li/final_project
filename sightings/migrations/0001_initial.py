# Generated by Django 2.2.7 on 2019-11-27 03:44

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
                ('unique_squirrel_id', models.CharField(max_length=200, unique=True)),
                ('shift', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('age', models.CharField(blank=True, max_length=200, null=True)),
                ('primary_fur_color', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('specific_location', models.CharField(blank=True, max_length=200, null=True)),
                ('running', models.BooleanField(blank=True, null=True)),
                ('chasing', models.BooleanField(blank=True, null=True)),
                ('climbing', models.BooleanField(blank=True, null=True)),
                ('eating', models.BooleanField(blank=True, null=True)),
                ('foraging', models.BooleanField(blank=True, null=True)),
                ('other_activities', models.CharField(blank=True, max_length=200, null=True)),
                ('kuks', models.BooleanField(blank=True, null=True)),
                ('quaas', models.BooleanField(blank=True, null=True)),
                ('moans', models.BooleanField(blank=True, null=True)),
                ('tail_flags', models.BooleanField(blank=True, null=True)),
                ('tail_twitches', models.BooleanField(blank=True, null=True)),
                ('approaches', models.BooleanField(blank=True, null=True)),
                ('indifferent', models.BooleanField(blank=True, null=True)),
                ('runs_from', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]