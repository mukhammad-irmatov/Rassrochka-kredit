# Generated by Django 3.2.6 on 2021-10-21 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='familiya',
            new_name='familiyasi',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='ism',
            new_name='ismi',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='telefon_nomer',
            new_name='telefon_raqami',
        ),
    ]
