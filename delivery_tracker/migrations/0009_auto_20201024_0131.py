# Generated by Django 3.1.2 on 2020-10-24 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_tracker', '0008_weight_cost_matrix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weight_cost_matrix',
            old_name='case_cost',
            new_name='base_cost',
        ),
    ]