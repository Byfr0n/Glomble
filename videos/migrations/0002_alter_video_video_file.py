
# Generated by Django 4.1.3 on 2022-11-05 15:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='uploads/video_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-05 15:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='uploads/video_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
