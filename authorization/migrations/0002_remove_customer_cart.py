# Generated by Django 3.2.8 on 2021-11-07 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cart',
        ),
    ]
