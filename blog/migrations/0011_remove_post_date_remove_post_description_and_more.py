# Generated by Django 5.0.3 on 2024-03-05 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_publicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='date',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='description',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='title',
        ),
    ]
