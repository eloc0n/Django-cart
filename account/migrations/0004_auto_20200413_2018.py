# Generated by Django 3.0.4 on 2020-04-13 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_useraddres_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddres',
            old_name='order_id',
            new_name='order',
        ),
    ]
