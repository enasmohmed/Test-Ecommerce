# Generated by Django 2.2.13 on 2021-12-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20211205_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Order Processing', 'Order Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Order Processing', max_length=100),
        ),
        migrations.DeleteModel(
            name='TrackOrder',
        ),
    ]
