# Generated by Django 3.2.6 on 2021-10-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_auto_20211021_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='familiyasi',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='telefon_raqami',
            field=models.IntegerField(),
        ),
    ]