# Generated by Django 5.1.7 on 2025-03-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_vehicle_rajaswo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='ijajat_no',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
