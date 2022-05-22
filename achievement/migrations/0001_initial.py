# Generated by Django 4.0.4 on 2022-05-22 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_percent', models.FloatField(default=0)),
                ('total_schedules_day', models.IntegerField(default=0)),
                ('finished_schedules_day', models.IntegerField(default=0)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='achievement_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
