# Generated by Django 4.0.4 on 2022-05-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_alter_schedule_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.CharField(choices=[('hp', '체력'), ('int', '지력'), ('will', '근성'), ('exp', '경험'), ('money', '재력'), ('ten', '행복')], default='will', max_length=8),
        ),
    ]
