# Generated by Django 3.1.2 on 2020-10-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_tracker', '0002_auto_20201021_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_type', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_time', models.CharField(max_length=20)),
            ],
        ),
    ]