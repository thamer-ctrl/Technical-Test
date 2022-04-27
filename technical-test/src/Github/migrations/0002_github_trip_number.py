# Generated by Django 4.0.4 on 2022-04-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Github', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='github',
            name='trip_number',
            field=models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='Trip Number'),
        ),
    ]