# Generated by Django 5.1.2 on 2024-11-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_receiver_usermessage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='is_viewed',
            field=models.BooleanField(default=False),
        ),
    ]
