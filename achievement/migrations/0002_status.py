# Generated by Django 4.0.4 on 2022-05-23 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.FloatField(default=0)),
                ('int', models.FloatField(default=0)),
                ('money', models.FloatField(default=0)),
                ('ten', models.FloatField(default=0)),
                ('exp', models.FloatField(default=0)),
                ('will', models.FloatField(default=0)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]