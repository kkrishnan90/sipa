# Generated by Django 4.1.1 on 2022-09-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_ordermodel_options_alter_ordermodel_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='qr_code',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='qr_code_img_url',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
