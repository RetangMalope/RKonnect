# Generated by Django 4.2.2 on 2023-07-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='Logo.png', null=True, upload_to=''),
        ),
    ]