# Generated by Django 3.2.7 on 2021-09-16 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0003_memory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memory',
            old_name='author',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='memory',
            old_name='created',
            new_name='timestamp',
        ),
    ]
