# Generated by Django 4.2.6 on 2023-11-09 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0008_employee_employee_class_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_Name', models.CharField(max_length=200)),
                ('Admin_Email', models.CharField(max_length=200)),
                ('Admin_Phone', models.IntegerField()),
                ('Facility_Name', models.CharField(max_length=200)),
                ('Facility_Address', models.CharField(max_length=200)),
                ('Facility_Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='child_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sign_In_Date', models.DateField()),
                ('Sign_Out_Date', models.DateField()),
                ('Sign_In_Time', models.TimeField()),
                ('Sign_Out_Time', models.TimeField()),
                ('Facility_Name', models.CharField(max_length=200)),
                ('Child_First_Name', models.CharField(max_length=200)),
                ('Child_Last_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='enrollments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Child_First_Name', models.CharField(max_length=200)),
                ('Child_Last_Name', models.CharField(max_length=200)),
                ('Classroom', models.CharField(max_length=200)),
                ('Tuition_Fee', models.IntegerField()),
                ('Teacher_First_Name', models.CharField(max_length=200)),
                ('Teacher_Last_Name', models.CharField(max_length=200)),
                ('Facility_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facility_Name', models.CharField(max_length=200)),
                ('Facility_Address', models.CharField(max_length=200)),
                ('Facility_Phone', models.IntegerField()),
                ('License_Number', models.IntegerField()),
                ('Admin_Name', models.CharField(max_length=200)),
                ('Admin_Email', models.CharField(max_length=200)),
                ('Admin_Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='parent',
            fields=[
                ('Parent_id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('Parent_First_Name', models.CharField(max_length=200)),
                ('Parent_Last_Name', models.CharField(max_length=200)),
                ('Parent_Phone', models.CharField(max_length=200)),
                ('Child_First_Name', models.CharField(max_length=200)),
                ('Child_Last_Name', models.CharField(max_length=200)),
                ('Child_DOB', models.DateField()),
                ('Child_Allergies', models.CharField(max_length=200)),
                ('Child_Address', models.CharField(max_length=200)),
                ('Sign_In_Date', models.DateField()),
                ('Sign_Out_Date', models.DateField()),
                ('Sign_In_Time', models.TimeField()),
                ('Sign_Out_Time', models.TimeField()),
                ('Facility_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='staff_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sign_In_Date', models.DateField()),
                ('Sign_Out_Date', models.DateField()),
                ('Sign_In_Time', models.TimeField()),
                ('Sign_Out_Time', models.TimeField()),
                ('Facility_Name', models.CharField(max_length=200)),
                ('Teacher_First_Name', models.CharField(max_length=200)),
                ('Teacher_Last_Name', models.CharField(max_length=200)),
                ('Hours_Worked', models.IntegerField()),
                ('Salary_Earned', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='child',
            name='Parent_FullName',
        ),
        migrations.RemoveField(
            model_name='child',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Employee_Class_Num',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Employee_DBO',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Employee_Phone_Number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Employee_Salary',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='child',
            name='Child_DoB',
            field=models.DateField(default='9999-12-31', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='Child_id',
            field=models.UUIDField(default=999, editable=False, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='Consent_Box',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='Parent_Address',
            field=models.CharField(default='000000', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='Parent_First_Name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='Parent_Last_Name',
            field=models.CharField(default='ppp', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='Parent_Phone',
            field=models.CharField(default='9999999', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='Classroom',
            field=models.CharField(default='a12', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='Employee_DOB',
            field=models.DateField(default='9999-12-31'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='Facility_Name',
            field=models.CharField(default='main', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='Hourly_Salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.UUIDField(default=0, editable=False, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='Employee_Address',
            field=models.CharField(default='999999', max_length=200),
            preserve_default=False,
        ),
    ]
