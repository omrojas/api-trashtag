# Generated by Django 3.0.6 on 2020-06-20 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbagecollector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('operation_area', models.CharField(max_length=100)),
                ('phone_one', models.CharField(max_length=12)),
                ('phone_two', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('manager_name', models.CharField(max_length=100)),
                ('manager_phone', models.CharField(max_length=12)),
                ('manager_email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Organizations',
            },
        ),
    ]
