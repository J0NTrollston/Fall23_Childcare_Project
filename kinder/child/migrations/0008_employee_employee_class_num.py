# Generated by Django 4.2.6 on 2023-11-01 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0007_alter_employee_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Employee_Class_Num',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
