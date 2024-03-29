# Generated by Django 5.0.2 on 2024-03-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AddField(
            model_name='post',
            name='media_file',
            field=models.FileField(blank=True, help_text='Upload an image or a video.', null=True, upload_to='blog/media/%Y'),
        ),
    ]
