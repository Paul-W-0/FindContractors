# Generated by Django 3.2.9 on 2021-12-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContractorApp', '0014_securityreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, max_length=220, null=True, unique=True),
        ),
    ]
