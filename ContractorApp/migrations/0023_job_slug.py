# Generated by Django 3.2.9 on 2022-01-07 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContractorApp', '0022_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]