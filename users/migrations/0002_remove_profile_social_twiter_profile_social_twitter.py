# Generated by Django 4.2.2 on 2023-07-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_twiter',
        ),
        migrations.AddField(
            model_name='profile',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
