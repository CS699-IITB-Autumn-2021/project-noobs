# Generated by Django 3.2.8 on 2021-10-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0016_auto_20211026_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='razorpay_order_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='razorpay_payment_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]