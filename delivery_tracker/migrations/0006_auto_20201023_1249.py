# Generated by Django 3.1.2 on 2020-10-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_tracker', '0005_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.AlterField(
            model_name='route',
            name='destination_area',
            field=models.CharField(default='uncategorized', max_length=8),
        ),
        migrations.AlterField(
            model_name='route',
            name='origin_area',
            field=models.CharField(default='uncategorized', max_length=8),
        ),
    ]
