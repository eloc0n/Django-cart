# Generated by Django 3.0.4 on 2020-04-13 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_useraddres_order'),
        ('order', '0009_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAddres', to='account.UserAddres'),
        ),
    ]
