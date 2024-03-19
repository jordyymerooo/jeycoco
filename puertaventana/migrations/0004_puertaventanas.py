# Generated by Django 5.0.3 on 2024-03-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puertaventana', '0003_rename_puertaventanas_doorswindows'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puertaventanas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='puertaventana/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='puertaventana/video/%Y')),
            ],
        ),
    ]
