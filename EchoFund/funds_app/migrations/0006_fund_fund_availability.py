# Generated by Django 5.1.2 on 2024-11-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds_app', '0005_fund_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='fund_availability',
            field=models.BooleanField(default=True),
        ),
    ]
