# Generated by Django 5.0.2 on 2024-03-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubiertas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cubiertas',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cubierta/images'),
        ),
        migrations.AlterField(
            model_name='cubiertas',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='cubierta/video/%Y'),
        ),
    ]