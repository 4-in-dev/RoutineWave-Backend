# Generated by Django 4.0.4 on 2022-05-23 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduletemplates', '0003_scheduletemplate_template_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduletemplate',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
