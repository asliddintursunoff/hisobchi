# Generated by Django 5.1.6 on 2025-03-06 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_attendence_date_day_alter_company_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 19, 54, 16, 937645, tzinfo=datetime.timezone.utc)),
        ),
    ]
