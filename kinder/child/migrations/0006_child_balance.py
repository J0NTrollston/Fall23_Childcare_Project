# Generated by Django 4.2.6 on 2023-11-27 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0005_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='Balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
