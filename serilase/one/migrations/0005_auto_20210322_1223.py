# Generated by Django 3.1.7 on 2021-03-22 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_auto_20210322_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='one.department'),
        ),
    ]
