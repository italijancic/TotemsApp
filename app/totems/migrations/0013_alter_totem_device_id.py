# Generated by Django 3.2.4 on 2021-06-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totems', '0012_totem_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totem',
            name='device_id',
            field=models.CharField(max_length=17, null=True, unique=True),
        ),
    ]
