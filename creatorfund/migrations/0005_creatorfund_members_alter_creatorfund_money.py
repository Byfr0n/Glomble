# Generated by Django 5.1.1 on 2024-10-10 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatorfund', '0004_creator_percentage_share_creatorfund_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatorfund',
            name='members',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='creatorfund.creator'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creatorfund',
            name='money',
            field=models.PositiveIntegerField(),
        ),
    ]
