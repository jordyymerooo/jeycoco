# Generated by Django 5.0.3 on 2024-03-05 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nieve', '0003_nieve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nieve',
            name='title',
        ),
        migrations.RemoveField(
            model_name='snow',
            name='title',
        ),
    ]
