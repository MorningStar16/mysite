# Generated by Django 3.1.5 on 2021-01-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_auto_20210108_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vc',
            name='date_closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
