# Generated by Django 4.1.7 on 2023-04-03 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile', verbose_name='Автор'),
        ),
    ]