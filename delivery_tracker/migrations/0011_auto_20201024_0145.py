# Generated by Django 3.1.2 on 2020-10-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_tracker', '0010_remove_delivery_request_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='package_type',
            field=models.CharField(choices=[('LTR', 'Letter'), ('PAR', 'Parcel'), ('PCK', 'Package'), ('BOX', 'Box')], default='LTR', max_length=3),
        ),
    ]