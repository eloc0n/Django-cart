# Generated by Django 3.0.4 on 2020-04-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20200413_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
