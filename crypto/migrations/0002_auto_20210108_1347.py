# Generated by Django 3.1.5 on 2021-01-08 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vc',
            old_name='Loss_Profit',
            new_name='amount_invested',
        ),
        migrations.RenameField(
            model_name='vc',
            old_name='amount',
            new_name='loss_profit',
        ),
    ]
