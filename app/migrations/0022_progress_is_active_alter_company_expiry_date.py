# Generated by Django 5.1.6 on 2025-03-04 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_company_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 19, 22, 52, 49, 876120, tzinfo=datetime.timezone.utc)),
        ),
    ]
