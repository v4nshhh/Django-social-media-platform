# Generated by Django 3.0.8 on 2021-05-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_app', '0002_auto_20210530_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogCreated',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]