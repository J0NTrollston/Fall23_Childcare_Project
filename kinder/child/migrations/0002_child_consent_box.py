# Generated by Django 4.2.6 on 2023-11-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='Consent_Box',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
