# Generated by Django 5.0.1 on 2024-02-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0011_llmconfig_use_docker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llmconfig',
            name='use_docker',
        ),
    ]