# Generated by Django 3.2.6 on 2022-11-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221105_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='blog/images/%Y/%m/%d/'),
        ),
    ]