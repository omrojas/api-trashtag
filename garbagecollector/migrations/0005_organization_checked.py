# Generated by Django 3.0.6 on 2020-07-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbagecollector', '0004_usermessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
