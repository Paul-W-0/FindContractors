# Generated by Django 3.2.9 on 2022-02-11 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ContractorApp', '0036_auto_20220211_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110)),
                ('description', models.TextField()),
                ('work_duties', models.TextField()),
                ('preferred_certifications', models.TextField()),
                ('minimum_qualifications', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('contractor_name', models.CharField(default='', max_length=175)),
                ('contractor_email', models.EmailField(max_length=254, null=True)),
                ('contractor_experience', models.TextField(null=True)),
                ('employer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='contractor_email',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='contractor_experience',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='contractor_name',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='description',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='employer',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='minimum_qualifications',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='preferred_certifications',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='title',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='work_duties',
        ),
        migrations.DeleteModel(
            name='NewHiree',
        ),
    ]
