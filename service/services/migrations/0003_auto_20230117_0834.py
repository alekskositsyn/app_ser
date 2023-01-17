# Generated by Django 3.2.16 on 2023-01-17 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_subscription_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='services.plan'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='services.service'),
        ),
    ]