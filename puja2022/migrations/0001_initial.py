# Generated by Django 4.1.1 on 2022-09-24 14:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Puja 2022',
            },
        ),
    ]
