# Generated by Django 3.1.7 on 2021-04-01 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_1', '0004_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20)),
                ('emp_reg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('emp_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_1.employee_model')),
            ],
        ),
    ]
