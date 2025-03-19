# Generated by Django 5.1.6 on 2025-03-06 19:22

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_attendence_date_month_alter_attendence_date_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence_date',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.worker'),
        ),
        migrations.AlterField(
            model_name='company',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 19, 22, 59, 314901, tzinfo=datetime.timezone.utc)),
        ),
    ]
