# Generated by Django 5.1.1 on 2024-10-10 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatorfund', '0003_alter_creator_paypal_email'),
        ('profiles', '0025_profile_passed_milestones'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='percentage_share',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CreatorFund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.AddField(
            model_name='creator',
            name='creator_fund',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='creatorfund.creatorfund'),
            preserve_default=False,
        ),
    ]