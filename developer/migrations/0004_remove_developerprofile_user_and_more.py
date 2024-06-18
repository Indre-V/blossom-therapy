# Generated by Django 4.2.13 on 2024-06-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0003_developerprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developerprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='developerprofile',
            name='certifications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='developerprofile',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='developerprofile',
            name='linkedin_profile_link',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='developerprofile',
            name='skills',
            field=models.TextField(blank=True),
        ),
    ]
