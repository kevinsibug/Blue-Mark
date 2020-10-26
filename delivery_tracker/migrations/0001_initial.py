# Generated by Django 3.1.2 on 2020-10-26 13:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_firstname', models.TextField()),
                ('staff_lastname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(choices=[('Letter', 'Letter'), ('Parcel', 'Parcel'), ('Package', 'Package'), ('Box', 'Box')], max_length=7)),
                ('package_weight', models.IntegerField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.TextField(primary_key=True, serialize=False)),
                ('origin_area', models.CharField(choices=[('Luzon', 'Luzon'), ('Visayas', 'Visayas'), ('Mindanao', 'Mindanao')], max_length=8)),
                ('destination_area', models.CharField(choices=[('Luzon', 'Luzon'), ('Visayas', 'Visayas'), ('Mindanao', 'Mindanao')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('Express', 'Express'), ('Ordinary', 'Ordinary')], max_length=8)),
                ('delivery_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Weight_Cost_Matrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_weight', models.FloatField(default=0.0)),
                ('base_cost', models.FloatField(default=0.0)),
                ('increment_weight', models.FloatField(default=0.0)),
                ('increment_cost', models.FloatField(default=0.0)),
                ('package_type', models.CharField(choices=[('Letter', 'Letter'), ('Parcel', 'Parcel'), ('Package', 'Package'), ('Box', 'Box')], max_length=7)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.route')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.service')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_Request',
            fields=[
                ('control_number', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField()),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.customer')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.package')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.recipient')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.route')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.service')),
                ('weight_cost_matrix', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.weight_cost_matrix')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_Receipt',
            fields=[
                ('control_number', models.AutoField(primary_key=True, serialize=False)),
                ('date_delivered', models.DateField(default=datetime.date.today)),
                ('consignee_signature', models.ImageField(upload_to='')),
                ('Delivery_Staff', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.delivery_staff')),
                ('delivery_request', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='delivery_tracker.delivery_request')),
            ],
        ),
    ]
