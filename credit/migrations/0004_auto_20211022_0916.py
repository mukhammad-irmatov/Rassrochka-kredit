# Generated by Django 3.2.6 on 2021-10-22 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20211022_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=50)),
                ('familiyasi', models.CharField(max_length=50)),
                ('telefon_raqami', models.IntegerField()),
                ('xabar', models.TextField()),
                ('xabar_yuborilgan_vaqt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Foydalanuvchilardan kelgan xabarlar',
                'ordering': ['xabar_yuborilgan_vaqt'],
            },
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]