# Generated by Django 3.2.7 on 2021-10-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_alter_product_avgreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userBuyedProducts',
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saleAddedDate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=50)),
                ('saleProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.product')),
                ('saleUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.user')),
            ],
        ),
    ]