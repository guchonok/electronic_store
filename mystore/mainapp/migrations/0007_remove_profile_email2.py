# Generated by Django 4.1.7 on 2023-04-02 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_profile_options_profile_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email2',
        ),
    ]
