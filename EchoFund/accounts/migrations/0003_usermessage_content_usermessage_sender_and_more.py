# Generated by Django 5.1.2 on 2024-11-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usermessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='content',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='sender',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='subject',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]