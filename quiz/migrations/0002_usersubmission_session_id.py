# Generated by Django 5.1.4 on 2024-12-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubmission',
            name='session_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]