# Generated by Django 3.0.8 on 2021-05-31 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_app', '0009_auto_20210531_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogCreated',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]