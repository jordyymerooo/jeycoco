# Generated by Django 5.0.3 on 2024-03-05 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revestimientos', '0002_siding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revestimientos',
            name='title',
        ),
        migrations.RemoveField(
            model_name='siding',
            name='title',
        ),
    ]