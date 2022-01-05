# Generated by Django 3.2.9 on 2021-12-23 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContractorApp', '0016_auto_20211223_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_number',
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=110), max_length=220, unique=True),
        ),
    ]
