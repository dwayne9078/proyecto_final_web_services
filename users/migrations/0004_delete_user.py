# Generated by Django 4.2.7 on 2023-12-11 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
