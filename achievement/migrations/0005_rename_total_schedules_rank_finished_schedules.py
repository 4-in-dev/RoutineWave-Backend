# Generated by Django 4.0.4 on 2022-05-27 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0004_rank_total_schedules'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rank',
            old_name='total_schedules',
            new_name='finished_schedules',
        ),
    ]