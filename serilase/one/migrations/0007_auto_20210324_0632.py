# Generated by Django 3.1.7 on 2021-03-24 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0006_auto_20210324_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='d_epartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='e_mployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.AddField(
            model_name='d_epartment',
            name='_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='one.e_mployee'),
        ),
    ]
