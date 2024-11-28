# Generated by Django 5.1.2 on 2024-11-28 20:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds_app', '0003_fund_fund_members_fund_fund_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='fund_members',
            field=models.ManyToManyField(blank=True, related_name='fund_members', to=settings.AUTH_USER_MODEL),
        ),
    ]