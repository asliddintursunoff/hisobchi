# Generated by Django 5.1.6 on 2025-03-11 22:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_alter_company_expiry_date_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 26, 22, 20, 55, 860069, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='DateforExpanse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.AddField(
            model_name='expanse',
            name='date',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.dateforexpanse'),
            preserve_default=False,
        ),
    ]
