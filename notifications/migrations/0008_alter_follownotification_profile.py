# Generated by Django 5.1.1 on 2024-10-10 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_follownotification_profile_likenotification_comment_and_more'),
        ('profiles', '0025_profile_passed_milestones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follownotification',
            name='profile',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='milestone_profile', to='profiles.profile'),
            preserve_default=False,
        ),
    ]
