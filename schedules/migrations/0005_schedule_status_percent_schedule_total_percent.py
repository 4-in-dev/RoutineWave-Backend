# Generated by Django 4.0.4 on 2022-05-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_alter_schedule_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='status_percent',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='total_percent',
            field=models.FloatField(default=0),
        ),
    ]
