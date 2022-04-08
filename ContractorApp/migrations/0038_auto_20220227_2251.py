# Generated by Django 3.2.9 on 2022-02-27 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ContractorApp', '0037_auto_20220211_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='contractor_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='contractor_experience',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='contractor_name',
            field=models.CharField(default='', max_length=175),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='employer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='minimum_qualifications',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='preferred_certifications',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='title',
            field=models.CharField(default='', max_length=110),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='work_duties',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
