# Generated by Django 3.2.9 on 2022-01-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContractorApp', '0033_alter_job_get_latest_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewHiree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='get_latest_by',
        ),
    ]
