# Generated by Django 2.2.10 on 2021-02-25 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0021_auto_20210205_0433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='official_program_reports',
            new_name='whos_working_on_what',
        ),
    ]