# Generated by Django 5.0.2 on 2024-03-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molduras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='molduras',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='moldura/images'),
        ),
        migrations.AlterField(
            model_name='molduras',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='moldura/video/%Y'),
        ),
    ]
