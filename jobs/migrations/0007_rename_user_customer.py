# Generated by Django 3.2 on 2021-09-13 04:17

from django.db import migrations


class Migration(migrations.Migration):


    dependencies = [
        ('jobs', '0005_alter_orderdetail_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
