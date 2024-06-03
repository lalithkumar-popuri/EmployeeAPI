# Generated by Django 5.0.3 on 2024-03-30 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressdetails',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='addressdetails',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='addressDetails', to='employeeAPI.employee'),
        ),
        migrations.AlterField(
            model_name='addressdetails',
            name='hno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='addressdetails',
            name='state',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addressdetails',
            name='street',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phoneNo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='projects',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='employeeAPI.employee'),
        ),
        migrations.AlterField(
            model_name='qualifications',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to='employeeAPI.employee'),
        ),
        migrations.AlterField(
            model_name='qualifications',
            name='qualificationName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='companyName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workExperience', to='employeeAPI.employee'),
        ),
    ]