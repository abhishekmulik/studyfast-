# Generated by Django 3.0.3 on 2020-11-11 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201110_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='New_Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='New_Subject',
        ),
    ]
