# Generated by Django 3.2.9 on 2022-04-08 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContractorApp', '0039_auto_20220301_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='email',
        ),
    ]
