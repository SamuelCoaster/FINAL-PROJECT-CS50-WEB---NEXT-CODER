# Generated by Django 3.2.6 on 2021-08-22 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nextCoder', '0003_alter_talks_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talks',
            name='tag2',
        ),
    ]
