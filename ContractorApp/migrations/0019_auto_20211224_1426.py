# Generated by Django 3.2.9 on 2021-12-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContractorApp', '0018_auto_20211223_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_number',
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(default=None, max_length=110, unique=True),
        ),
    ]
