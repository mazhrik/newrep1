# Generated by Django 3.1.7 on 2021-03-30 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_reg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_name', models.CharField(max_length=30)),
                ('info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_1.student_model')),
            ],
        ),
    ]
