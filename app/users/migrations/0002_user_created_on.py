# Generated by Django 3.2.4 on 2021-06-15 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
