# Generated by Django 5.0.1 on 2024-02-06 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_rename_llm_config_agent__llm_config'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='_llm_config',
            new_name='llm_config',
        ),
    ]
